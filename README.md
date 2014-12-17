# Code Summany
The code for this project contain about two part:
one is for analyzing historical data, and other is for real time data.

## Data File
when we create some data we want to analyze, we put them into __data__ file 

## Historical Analyse
for this part, we have __5__ directories:

1. __anaylyze&draw__: When we get data from hive, we use the scripts in this directory to further analyse and do data visualizaiton.
2. __clean__: The scripts in this directory are that we use to get extra information which is not in original data and further clean that data.
3. __get_data_from_hive__: This directory includes some hive and shell script to get data which we want from original data.
4. __graph__: This directory include all _HTML_ files which include __D3.js__ to get visualize data.(note the files are not the same as the files in __anaylyze&draw__).
5. __animation__: This directory include _Processing_ code to make animation for NYC check-in on 10/09/2012.

## Realtime Analyse
for this part, we have __2__  directories:

1. __heatmap__: This directory include code for creating check-in heatmap for realtime data.
2. __real_time_frequency__: This file include code for creating every two second frequency for realtime data. 





