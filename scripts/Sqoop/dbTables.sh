sqoop list-databases \
--connect jdbc:mysql://localhost:3306 \
--connection-manager org.apache.sqoop.manager.MySQLManager \
--username=root \
--password=$HADOOP_PASS

sqoop list-tables \
--connect jdbc:mysql://localhost:3306/movielens \
--connection-manager org.apache.sqoop.manager.MySQLManager \
--username=root \
--password=$HADOOP_PASS