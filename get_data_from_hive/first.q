create external table w1(userid bigint, tweetid bigint, latitude double, longtitude double, time timestamp, text string, placeid string)
row format delimited fields terminated by '\t'
location '/user/cw1733/hiveinput/';

hive -e 'select latitude, longtitude from w1' > total.tsv
hive -e 'select latitude, longtitude from w1 where latitude >= 18.005611 and latitude <= 48.987386 and longtitude >= -124.626080 and longtitude <= -62.361014' > us.tsv

hive -e 'select latitude, longtitude from w1 where latitude >= 40.47739900000000 and latitude <= 40.91757700000000 and longtitude >= -74.25909000000000 and longtitude <= -73.70027200000000' > nyc.tsv