import datetime
out = open('check_in_hour.tsv', 'w')
with open('nyc_10_09_all.tsv', 'r') as f:
	while True:
		content = f.readline()
		if not content: break
		temp = content.split('\t')
#		2010-10-09 00:00:08
		date = datetime.datetime.strptime(temp[4], "%Y-%m-%d %H:%M:%S")
		hour = date.hour
		print hour
		out.write(temp[2] + '\t' + temp[3] + '\t' + str(hour) + '\t' + temp[5] + '\n')
			
out.close()