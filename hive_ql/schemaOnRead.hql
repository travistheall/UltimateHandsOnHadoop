-- maintains a metastore that imparts a structure you define 
-- on the unstructured data that is stored on the HDFS
CREATE TABLE ratings (
  userID INT,
  movieID INT,
  rating INT,
  time, INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE;

LOAD DATA LOCAL INPATH `${env:HOME}/data/u.data`
OVERWRITE INTO TABLE ratings;
