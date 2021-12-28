#!bin/bash
sqoop export \
--connect jdbc:mysql://localhost/movielens \
-m 1 \
--driver com.mysql.jdbc.Driver \
--table exported_movies \
--export_dir /apps/hive/warehouse/movies \
--input-fields-terminated-by '\0001'

# target must exist in mysql