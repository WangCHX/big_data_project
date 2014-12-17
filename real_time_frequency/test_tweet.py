from TwitterAPI import TwitterAPI, TwitterRestPager
from datetime import datetime, date
import bitly_api
import urllib2, json
import httplib

from pymongo import MongoClient

connection = MongoClient()

db = connection['foursquare']

# col = db.create_collection('check_in', capped=True,size=20000)
col = db.create_collection('check_in')



CONSUMER_KEY = 'yp0Onn7MprXj5IZDaOL57dyvQ'
CONSUMER_SECRET = 'L4KDkeFlvJM3u3208VgXZ3gTiaWlGOtKvjIqhvNIAoPcYZ7yfs'
ACCESS_TOKEN_KEY = '2321306595-G9Qr4XmivVfyTuqLKmadZxLVlyL9OgyV4HgxNIZ'
ACCESS_TOKEN_SECRET = '0tX8VhWOioxJ3fQtThAHKolhkbDPS5UtRSfjteyZJQdix'







api = TwitterAPI(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN_KEY,ACCESS_TOKEN_SECRET)



# pager = TwitterRestPager(api, 'search/tweets', {'q': SEARCH_TERM})
# pager = api.request('statuses/filter', {'locations':'-74,40,-73,41'})
pager = api.request('statuses/sample')
# pager = api.request('search/tweets', {'q':SEARCH_TERM})


for item in pager.get_iterator():
    # print item
    if 'timestamp_ms' in item:
        created_at = long(item['timestamp_ms']) / 1000 % 1000
        # print created_at
        temp = {'created_at':created_at, 'count' : 1}
        cursor = list(col.find({'created_at':{"$in":[created_at]}}))
        if not cursor:
            print 'xxxx'
            col.insert(temp)
        for p in cursor:

            prev = p['count']
            print prev
            col.update({'_id':p['_id']},{'$inc':{'count': 1}},upsert=False, multi=False)
        print temp

