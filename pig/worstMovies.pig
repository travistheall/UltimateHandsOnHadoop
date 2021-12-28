/*
For Ambari
ratings = LOAD '/user/maria_dev/data/u.data' AS (userID:int, movieID:int, rating:int, ratingTime:int);
metadata = LOAD '/user/maria_dev/data/u.item' USING PigStorage('|') AS (movieID:int, movieTitle:chararray, releaseDate:chararray, videoRelease:chararray, imdbLink:chararray);
*/
ratings = LOAD '/home/maria_dev/data/u.data' AS (userID:int, movieID:int, rating:int, ratingTime:int);
metadata = LOAD '/home/maria_dev/data/u.item' USING PigStorage('|') AS (movieID:int, movieTitle:chararray, releaseDate:chararray, videoRelease:chararray, imdbLink:chararray);
nameLookup = FOREACH metadata GENERATE movieID, movieTitle, ToUnixTime(ToDate(releaseDate, 'dd-MMM-yyyy')) AS releaseTime;
ratingsByMovie = GROUP ratings BY movieID;
avgRatings = FOREACH ratingsByMovie GENERATE group AS movieID, AVG(ratings.rating) AS avgRating, COUNT(ratings.rating) AS ratingCount;
oneStarMovies = FILTER avgRatings BY avgRating < 2.0;
oneStarMoviesWithData = JOIN oneStarMovies BY movieID, nameLookup BY movieID;
worstMovies = ORDER oneStarMoviesWithData BY oneStarMovies::ratingCount DESC;
DUMP worstMovies;