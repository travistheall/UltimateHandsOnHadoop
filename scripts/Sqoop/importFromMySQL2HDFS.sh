#!bin/bash
sqoop import \
--connect jdbc:mysql://localhost/movielens \
--driver com.mysql.jdbc.Driver \
--table movies \
-m 1
