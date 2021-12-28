#!/bin/bash
cd /home/maria_dev/python/Spark
for f in *.py
do
 spark-submit $f
done
cd /home/maria_dev/scripts/Spark
