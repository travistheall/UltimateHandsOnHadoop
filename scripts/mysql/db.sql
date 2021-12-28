create database movielens;
show databases;
SET NAMES 'utf8';
SET CHARACTER SET utf8;
use movielens;
-- make sure you are in directory /home/maria_dev/data/sql/
source movielens.sql;
SELECT * FROM movies LIMIT 10;