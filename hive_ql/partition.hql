-- Store data in paritioned subdirectories
-- Huge optimization if queries are only on certain partitions
CREATE TABLE customers (
  name STRING,
  address STRUCT<street:STRING, city:STRING, state:STRING, zip:INT>
)
PARTITIONED BY (country STRING)
-- actual file locations
-- ../customers/country=CA/
-- ../customers/coutnry-GB/