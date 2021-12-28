from pyspark.sql import SparkSession
from util import Util

if __name__ == "__main__":
    u = Util(spark_version=2, name="LowestRatedMovieDataFrame")
    # Create a SparkSession (the config bit is only for Windows!)
    spark = SparkSession.builder.appName(u.name).getOrCreate()
    # Get the raw data
    lines = spark.sparkContext.textFile(u.hdfs_file)
    # Convert it to a RDD of Row objects with (movieID, rating)
    movies = lines.map(u.parseInput)
    # Convert that to a DataFrame
    movieDataset = spark.createDataFrame(movies)
    # Compute average rating for each movieID
    averageRatings = movieDataset.groupBy("movieID").avg("rating")
    # Compute count of ratings for each movieID
    counts = movieDataset.groupBy("movieID").count()
    # Join the two together (We now have movieID, avg(rating), and count columns)
    averagesAndCounts = counts.join(averageRatings, "movieID")
    # Pull the top 10 results
    topTen = averagesAndCounts.orderBy("avg(rating)").take(10)
    # Print them out, converting movie ID's to names as we go.
    u.create_out_file(top=topTen)
    # Stop the session
    spark.stop()
