from pyspark import SparkConf, SparkContext
from util import Util


if __name__ == "__main__":
  u = Util(spark_version=1, name="LowestRatedMovieSpark")
  conf = SparkConf().setAppName(u.name)
  sc = SparkContext(conf=conf)
  # load data file
  # in hadoop cluster
  # RDD object
  lines = sc.textFile(u.hdfs_file)
  # convert to (movieID, (rating, 1.0))
  # new RDD
  movieRatings = lines.map(u.parseInput)
  # reduce to (movieID, (sumOfRatings, totalRatings))
  ratingTotalsAndCount = movieRatings.reduceByKey(lambda movie1, movie2: (movie1[0] + movie2[0], movie1[1] + movie2[1]))
  # map to (movieID, averageRating)
  averageRatings = ratingTotalsAndCount.mapValues(lambda totalAndCount : totalAndCount[0] / totalAndCount[1])
  # sort by average ratings
  sortedMovies = averageRatings.sortBy(lambda x: x[1])
  # only the top 10
  topTen = sortedMovies.take(10)
  u.create_out_file(top=topTen)

