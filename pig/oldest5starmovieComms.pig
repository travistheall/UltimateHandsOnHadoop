ratings = LOAD '/home/maria_dev/data/u.data' AS (userID:int, movieID:int, rating:int, ratingTime:int); --creates relation named "ratings" gives the following schema
/* 
yields a tuple of the lines of u.data 
(0,50,5,881250949)
(0,172,5,881250949)
...etc
*/
metadata = LOAD '/home/maria_dev/data/u.item' USING PigStorage('|') AS (movieID:int, movieTitle:chararray, releaseDate:chararray, videoRelease:chararray, imdbLink:chararray);
-- DUMP metadata; -- like print(metadata)
/*
(1,Toy Story (1995),,01-Jan-1995,,http://us.imdb.com/M/title-exact?Toy%20Story%20(1995))
(2,GoldenEye (1995),,01-Jan-1995,,http://us.imdb.com/M/title-exact?GoldenEye%20(1995))
...etc
*/
nameLookup = FOREACH metadata GENERATE movieID, movieTitle, ToUnixTime(ToDate(releaseDate, 'dd-MMM-yyyy')) AS releaseTime;
/*
also got ride of imdbLink
(1,Toy Story (1995),788918400)
etc
*/
ratingsByMovie = GROUP ratings BY movieID;
/*
DUMP ratingsByMovie;
(1,{(807,1,4,892528231),(554,1,3,876231938),...etc})
*/
avgRatings = FOREACH ratingsByMovie GENERATE group AS movieID, AVG(ratings.rating) AS avgRating;
/*
DUMP avgRatings;
(1,3.8783185840707963)
(2,3.21...)
etc
DESCRIBE ratings;
-- ratings: {userID:int, movieID:int, rating:int, ratingTime:int}
DESCRIBE ratingsByMovie;
-- ratingsByMovie: {group:int, ratings:{(userID:int, movieID:int, rating:int, ratingTime:int)}}
DESCRIBE avgRatings;
-- avgRatings: {movieID:int, avgRating:double}
*/
fiveStarMovies = FILTER avgRatings BY avgRating > 4.0;
-- (12,4.3857677902621733) etc
DESCRIBE fiveStarMovies;
-- fiveStarMovies: {movieID:int, avgRating:double}
DESCRIBE nameLookup;
-- nameLookup:{movieID:int,movieTitle:chararray,releaseTime:long}
fiveStarMoviesWithData = JOIN fiveStarMovies BY movieID, nameLookup BY movieID;
DESCRIBE fiveStarMoviesWithData;
--table::column:datatype
--fiveStarMoviesWithData:{fiveStarMovies::movieId: int,fiveStarMoviesWithData::avgRating:double,nameLookup::movieID:int,nameLookup::movieTitle:chararray,nameLookup::releaseTime:long}
DUMP fiveStarMoviesWithData;
-- (12,4.38...,12,Usual Suspects, The (1995),808358400) etc
oldestFiveStarMovies = ORDER BY fiveStarMoviesWithData BY nameLookup::releaseTime;
DUMP oldestFiveStarMovies;
-- (493,4.15,493,"Thin Man,The (1934)", -1136073600)