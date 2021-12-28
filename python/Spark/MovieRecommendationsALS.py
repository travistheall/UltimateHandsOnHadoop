from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
from pyspark.sql.functions import lit
from util import Util


if __name__ == "__main__":
    u = Util(spark_version=2, name="MovieRecommendationsALS")
    # Create a SparkSession (the config bit is only for Windows!)
    spark = SparkSession.builder.appName(u.name).getOrCreate()
    # This line is necessary on HDP 2.6.5:
    spark.conf.set("spark.sql.crossJoin.enabled", "true")
    # Get the raw data
    lines = spark.read.text(u.hdfs_file).rdd
    # Convert it to a RDD of Row objects with (userID, movieID, rating)
    ratingsRDD = lines.map(u.parseInput)
    # Convert to a DataFrame and cache it
    ratings = spark.createDataFrame(ratingsRDD).cache()
    # Create an ALS collaborative filtering model from the complete data set
    als = ALS(maxIter=5, regParam=0.01, userCol="userID", itemCol="movieID", ratingCol="rating")
    model = als.fit(ratings)
    userRatings = ratings.filter("userID = 0")
    topRecommendations = userRatings.collect()
    u.create_out_file(top=topRecommendations, user=True)
    # Find movies rated more than 100 times
    ratingCounts = ratings.groupBy("movieID").count().filter("count > 100")
    # Construct a "test" dataframe for user 0 with every movie rated more than 100 times
    popularMovies = ratingCounts.select("movieID").withColumn('userID', lit(0))
    # Run our model on that list of popular movies for user ID 0
    recommendations = model.transform(popularMovies)
    # Get the top 20 movies with the highest predicted rating for this user
    topRecommendations = recommendations.sort(recommendations.prediction.desc()).take(20)
    u.create_out_file(top=topRecommendations)

    spark.stop()
