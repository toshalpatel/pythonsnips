import json
from pprint import pprint
import re
import __init__
#import requests
import google

with open('APTnotes.json') as data_file:    
    data = json.load(data_file)

#r= request.get("https://raw.githubusercontent.com/aptnotes/data/master/APTnotes.json")
#data = r.json()
	
i=0
titles = []

for element in data:
	titles.append(data[i]['Title'])
	#pprint(titles[i])
	i=i+1

#titles = set(titles)

#for title in titles:

print titles[3]
search_results = google.Google.search(titles[3])
for searchresults in search_results:
	print searchresults.link
