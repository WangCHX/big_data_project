from datetime import datetime, date
#import bitly_api
import foursquare
import urllib2, json
import httplib



BITLY_USERNAME = 'o_p00h7vd5h'
BITLY_API_KEY = 'R_19bff5294a094749a4177d9f639b7637'
BITLY_ACCESS_TOKEN = 'c6869fe932e2b5b912d97382c885fb8df8ba2bd8'

#FOURSQUARE_ACCESS_TOKEN = 'K44DQZABARQM2HM2ETXZZHLXY11KYXAHAKY3NB0BN15KBN0Z'

FOURSQUARE_ACCESS_TOKEN = 'X5LZHWIDTBTJCQ42RNCVVOSE3G15QPCVZUWLQXBKPADB13MW'
CLIENT_ID = 'P3UD132RIAGIIGSAAX2AB4E32KSTAGBZXPSSOKK1O3W22KNF'
CLIENT_SECRET = 'ZBHOZRYVRXSJ0CS3B4RPFCJSBFKSKGBEVLLZXEA144OJBB2D'


#def get_checkid_and_s(url):
#	checkin_index = url.find('checkin')
#	mark_s_index = url.find('?s=')
#	check_id = url[checkin_index + 8: mark_s_index]
#	refer_ref_index = url.find('&ref')
#	signature_id = url[mark_s_index + 3: refer_ref_index]
#	
#	return check_id, signature_id


def get_venue_id(url):
	index = url.rfind('/')
	return url[index:]

i = 0
def get_check_in_info(id):
	global i
	dt = date.today()
#	url = "https://api.foursquare.com/v2/venues/" + id + '?oauth_token=' + FOURSQUARE_ACCESS_TOKEN + '&v=' + dt.strftime('%Y%m%d')
	client = foursquare.Foursquare(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
	data = dict(client.venues(id))
#	print url
#	data = json.load(urllib2.urlopen(url))
	checkin = data['venue']
#	date_info = checkin['createdAt']
	timezoneoffset = checkin['timeZone']
	location = checkin['location']
	lat = location['lat']
	lng = location['lng']
	categories = checkin['categories']
	categories_name = ""
	for item in categories:
		categories_name += item['name'] + '\n'
#	print user_id, lat, lng, date_info, categories_name
	temp = str(lat) + '\t' + str(lng) + '\t' + categories_name + '\n'
	print temp
	with open("test.txt", "a") as myfile:
		i += 1
		print i
		myfile.write(categories_name + '\n')
		
source_file = 'nyc_m9.tsv'
with open(source_file, 'r') as data:
	while True:
		content1 = data.readline()
		if not content1: break
#		print content1
		line = ''.join(content1)
		
		index_first = line.find('http://4sq')
		if index_first != -1:
			index_end = line.find('\t', index_first)
			url = line[index_first: index_end]
			print url
			try:
				expanded_url = urllib2.urlopen(url).geturl()
				print expanded_url
				venue_id = get_venue_id(expanded_url)
				get_check_in_info(venue_id)
			except urllib2.HTTPError, e:
				print 'HTTPError = ' + str(e.code)
				pass
			except urllib2.URLError, e:
				print 'URLError = ' + str(e.reason)
				pass
			except httplib.HTTPException, e:
				print 'HTTPException'
				pass
			except Exception:
				import traceback
				print 'generic exception: ' + traceback.format_exc()
				pass
			