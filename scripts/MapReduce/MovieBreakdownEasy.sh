#!/bin/bash
python \
/home/maria_dev/python/MapReduce/MovieBreakdownEasy.py \
-r hadoop \
--hadoop-streaming-jar \
/usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
/home/maria_dev/data/u.data >\
/home/maria_dev/data/out/MapReduce/MovieBreakdownEasy.data