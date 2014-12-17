create external table w2 (userid bigint, statuscount bigint, followerscount bigint, friendscount bigint) row format delimited fields terminated by '\t' location '/user/cw1733/hiveinput2'; 

create table nyc_count as select userid, count(*) as user_check_in_count from nyc group by userid; 

create table check_in_num_friend as select nyc_count.user_check_in_count, w2.* from nyc_count join w2 on (nyc_count.userid = w2.userid)

hive -e "select * from check_in_num_friend" > check_in_num_friend.tsv