create database movielens;
show databases;
SET NAMES 'utf8';
SET CHARACTER SET utf8;
use movielens;
-- make sure you are in directory /home/maria_dev/data/sql/
source movies.sql;
source genres.sql;
source users.sql;
source occupations.sql;
source create_ratings.sql;
source ratings1.sql;
source ratings2.sql;
source ratings3.sql;
source ratings4.sql;
source ratings5.sql;
source ratings6.sql;
source ratings7.sql;
source ratings9.sql;
source ratings10.sql;
source ratings11.sql;
source genres_movies.sql;
source 
SELECT * FROM movies LIMIT 10;