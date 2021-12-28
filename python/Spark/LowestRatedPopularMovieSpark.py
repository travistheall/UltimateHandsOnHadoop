from pyspark import SparkConf, SparkContext
from util import Util


if __name__ == "__main__":
    u = Util(spark_version=1, name="LowestRatedPopularMovieSpark")
    # The main script - create our SparkContext
    conf = SparkConf().setAppName(u.name)
    sc = SparkContext(conf = conf)
    # Load up the raw u.data file
    lines = sc.textFile(u.hdfs_file)
    # Convert to (movieID, (rating, 1.0))
    movieRatings = lines.map(u.parseInput)
    # Reduce to (movieID, (sumOfRatings, totalRatings))
    ratingTotalsAndCount = movieRatings.reduceByKey(lambda movie1, movie2: ( movie1[0] + movie2[0], movie1[1] + movie2[1] ) )
    # Filter out movies rated 10 or fewer times 
    # x[1] = (sumOfRatings, totalRatings)
    # x[1][1] = totalRatings
    popularTotalsAndCount = ratingTotalsAndCount.filter(lambda x: x[1][1] > 10)
    # Map to (rating, averageRating)
    averageRatings = popularTotalsAndCount.mapValues(lambda totalAndCount : totalAndCount[0] / totalAndCount[1])
    # Sort by average rating
    sortedMovies = averageRatings.sortBy(lambda x: x[1])
    # Take the top 10 results
    topTen = sortedMovies.take(10)
    u.create_out_file(top=topTen)
