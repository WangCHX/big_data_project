create external table keyWord (word string) location '/user/cw1733/hiveinput3'

create table keyword_new as select * from keyWord where word != "";

create table keyword_num as select word, count(*) as num from keyword_new group by word order by num DESC;

hive -e "select * from keyword_num;" | sed 's/[\t]/,/g' > num.tsv

create table daily_checkin as select to_date(time) as date, count(*) as cnt from check_in group by to_date(time) order by cnt DESC;

create table nyc_daily_checkin as select to_date(time) as date, count(*) as cnt from nyc group by to_date(time) order by cnt DESC;

create table nyc_10_09 as select * from nyc where to_date(time) = "2010-10-09" order by time;


hive -e "select * from daily_checkin;" > daily_checkin.tsv

hive -e "select * from nyc_daily_checkin;" > nyc_daily_checkin.tsv

hive -e "select latitude, longitude, hour(time) from nyc_10_09;" > nyc_10_09_hour.tsv