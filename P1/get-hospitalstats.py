import json
import os
import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

noURLcounter = 0
hospitalcounter = 0
citycounter = 0

files = {}
wrongfiles = []
goodfiles = []
root = ''
# Traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("./collection/"):
    continue

# Drop error files, keep good files
for filename in files:
    if filename.startswith('error') or not filename.endswith('.json'):
        wrongfiles.append(filename)
    else:
        goodfiles.append(filename)

for filename in goodfiles:
    filename = './collection/' + filename
    with open(filename, 'r') as f:
        data = json.load(f)
	
    response = data['response']
    citycounter += 1
	
    for venue in response['venues']:
	    hospitalcounter += 1
	    referralId = venue['referralId']
	    name = venue['name']
	    latitude = venue['location']['lat']
	    longitude = venue['location']['lng']
	    url = '/'
    
	    if 'url' not in venue:
			noURLcounter += 1
	    else:
	        url = venue['url']
	
	    #sys.stdout.write("{0} - {1} - ({2}, {3}) - {4}".format(referralId, name, latitude, longitude, url))
		
print("Amount of cities inspected: {0}".format(citycounter))
print("Amount of cities NOT inspected: {0}".format(len(wrongfiles)-citycounter))	
print("Amount of (potential duplicate) hospitals found: {0}".format(hospitalcounter))
print("Amount of (potential duplicate) hospitals that do not have a URL: {0}".format(noURLcounter))