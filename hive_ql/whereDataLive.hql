-- LOAD DATA
--    MOVES  data from a distributed filesystem into HIVE
-- LOAD DATA LOCAL
--    COPIES data from your local filesystem into HIVE
-- MANAGED TABLE = when it is into HIVE and HIVE has it
-- above will be deleted from hdfs if deleted
-- EXTERNAL TABLE = when it's on the normal filesystems

CREATE EXTERNAL TABLE IF NOT EXISTS ratings (
  userID INT,
  movieID INT,
  rating INT,
  time, INT
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
LOCATION `/data/u.data`;
