# Type hint not supported in py2.7
def loadMovieNames() -> dict[int: str]:
  """
  cretate python diction that is used to convert movieIds to movie names
  then prints the final results
  from local disk
  """
  movieNames: dict[int: str] = {}
  with open('/home/maria_dev/data/u.item') as file:
    for line in file:
      fields = line.split('|')
      movieID: int = int(fields[0])
      movieTitle: str = fields[1]
      movieNames[movieID] = movieTitle
  return movieNames
  

def parseInput(line: str) -> tuple(int, (float, float)):
  """
  take each line of u.data and convert it to movieId, (rating,1.0)
  can add up all the ratings for each movie
  total number of ratings for each movie which lets us get the average
  """
  fields: list[str] = line.split()
  movieID: int = int(fields[1])
  rating: float = float(fields[2])
  value: float  = 1.0
  return(movieID, (rating, value))
