#!/bin/bash
python \
/home/maria_dev/python/RatingsBreakdown.py \
-r hadoop \
--hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
/home/maria_dev/data/u.data >\
/home/maria_dev/data/out/RatingsBreakdown.data
