import json
d = {}
with open('category.txt', 'r') as f:
	while True:
		content = f.readline()
		if not content: break
		cat = content.split('\t')[1]
#		print cat.split(',')
		for item in cat.split(',')[:-1]:
			d.setdefault(item, 0)
			d[item] += 1


import operator
#x = {1: 2, 3: 4, 4:3, 2:1, 0:0}
sorted_d = sorted(d.items(), key=operator.itemgetter(1))

dic = dict()
dic["name"] = "flare"
dic["children"] = []

subdic = dict()
count = 0

for key, value in sorted_d:
    if count == 0:
        subdic["name"] = key
        subdic["children"] = []
    if value > 100:
        item = dict()
        item["name"] = key
        item["size"] = value
        subdic["children"].append(item)
        count = count + 1
    if count == 5:
        dic["children"].append(dict(subdic))
        count = 0
if count != 0:
    dic["children"].append(dict(subdic))
    



out = open('cat.json', 'w')
out.write(json.dumps(dic))