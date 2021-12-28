from pyspark.sql import Row


class Util(object):
  def __init__(self, spark_version, name):
    self.uItem = "/home/maria_dev/data/u.item"
    self.hdfs_file = "hdfs:///user/maria_dev/data/u.data"
    self.spark_version = spark_version
    self.name = name
    self.data_out_file = "/home/maria_dev/data/out/Spark/" + self.name + ".data"
    self.movieNames = self.loadMovieNames()    
  
  def loadMovieNames(self):
    """
    cretate python diction that is used to convert movieIds to movie names
    then prints the final results
    from local disk
    """
    movieNames = {}
    with open(self.uItem) as file:
      for line in file:
        fields = line.split("|")
        movieID = int(fields[0])
        if self.name == "MovieRecommendationsALS":          
          movieTitle = fields[1].decode('ascii', 'ignore')
        else:
          movieTitle = fields[1]
        
        movieNames[movieID] = movieTitle

    return movieNames
    

  def parseInput(self, line):
    if self.name == "MovieRecommendationsALS":
      fields = line.value.split()
    else:
      fields = line.split()
    userID = int(fields[0])
    movieID = int(fields[1])
    rating = float(fields[2])
    if self.spark_version == 1:
      """
      Spark I
      take each line of u.data and convert it to movieId, (rating,1.0)
      can add up all the ratings for each movie
      total number of ratings for each movie which lets us get the average
      """
      value = 1.0
      row = movieID, (rating, value)
    elif self.spark_version == 2 and self.name != "MovieRecommendationsALS":
      """
      Spark II
      same as above but puts into a dataframe
      """
      row = Row(movieID=movieID, rating=rating)
    else:
      row = Row(userID=userID, movieID=movieID, rating=rating)
    return row
  
  def create_out_file(self, top, user=False):
    with open(self.data_out_file, 'a') as out_file:
      if user:
        out_file.write("Ratings for user ID 0:\n")

      for movie in top:
        if user:
          movieTitle = self.movieNames[movie['movieID']] 
          rating = movie['rating']
          line = "(" + str(movieTitle) + ", "+ str(rating) + ")\n"
        else:
          if self.name == "MovieRecommendationsALS":
            movieTitle = self.movieNames[movie['movieID']]
            prediction = movie['prediction']
            line = "(" + str(movieTitle) + ", "+ str(prediction) + ")\n"
          else:
            movieTitle = self.movieNames[movie[0]]
            avg_rating = movie[1]
            if self.spark_version == 1:
              line = "(" + str(movieTitle) + ", "+ str(avg_rating) + ")\n"
            elif self.spark_version == 2:
              count = movie[2]
              line = "(" + str(movieTitle) + ", "+ str(avg_rating) + ", " + str(count) + ")\n"

        out_file.write(line)

      if user:
        out_file.write("\nTop 20 recommendations:\n")
    