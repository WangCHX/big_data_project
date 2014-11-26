create external table keyWord (word string) location '/user/cw1733/hiveinput3'

create table keyword_new as select * from keyWord where word != "";

create table keyword_num as select word, count(*) as num from keyword_new group by word order by num DESC;

hive -e "select * from keyword_num;" | sed 's/[\t]/,/g' > num.tsv