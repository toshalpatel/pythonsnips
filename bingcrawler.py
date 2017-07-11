import json
from pprint import pprint
from py_ms_cognitive import PyMsCognitiveWebSearch
import urllib2
import urlparse

with open('APTnotes.json') as data_file:    
    data = json.load(data_file)

#r= request.get("https://raw.githubusercontent.com/aptnotes/data/master/APTnotes.json")
#data = r.json()
    
titles = []

for element in data:
    titles.append(element['Title'])
    #pprint(titles[i])

fhandle = open('bing_search_results.json','w')
#print titles[3]
urls = []
url_result = []

for title in titles:
    search_term = title
    #print(search_term)
    search_service = PyMsCognitiveWebSearch('c6b756d3b3714362bb690e9520421879', search_term)
    first_five_result = search_service.search(limit=5, format='json')

    for result in first_five_result:
        bing_result = json.dumps(result.json)
        #print(result.json['url'])
        fhandle.write(bing_result +'\n')
        url = result.json['url']
        urls.append(url)
        #print bing_result + '\n'
        
fhandle.close()
fhand = open('bing_urls.txt', 'w')

for url in urls:
    parsed = urlparse.urlparse(url)
    params = dict(urlparse.parse_qsl(parsed.query))
    url_result.append(params['r'])
    fhand.write(params['r']+'\n')
    #print params['r']
fhand.close()

print 'done!'
