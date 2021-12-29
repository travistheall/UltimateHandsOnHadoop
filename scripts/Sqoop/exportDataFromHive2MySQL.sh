#!/bin/bash
# both of these don't work. IDK why
sqoop export \
--connect jdbc:mysql://localhost:3306/movielens \
--driver com.mysql.jdbc.Driver \
-m 1 \
--table exported_movies \
--export-dir /apps/hive/warehouse/movies/ \
--input-fields-terminated-by '\0001'

sqoop export \
--connect jdbc:mysql://localhost:3306/movielens \
--connection-manager org.apache.sqoop.manager.MySQLManager \
--username=root \
--password=$HADOOP_PASS \
--export-dir /apps/hive/warehouse/movies \
--table exported_movies 