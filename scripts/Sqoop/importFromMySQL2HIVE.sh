#!bin/bash
sqoop import \
--connect jdbc:mysql://localhost/movielens \
--driver com.mysql.jdbc.Driver \
--table movies \
-m 1 \
--hive-import
# link to fix
# file modified @ /etc/hive/conf/hive-site.xml
# https://community.cloudera.com/t5/Support-Questions/Sqoop-Import-Error-User-null-does-not-belong-to-Hadoop-at/td-p/202547