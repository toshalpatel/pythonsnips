import tldextract

filename = "links_securityaffairs.txt"
fhandle = open(filename, "r")
urls = []

for line in fhandle:
	dom = tldextract.extract(line)
	if dom.domain != "wp":
		urls.append(line)
fhandle.close()
urls = set(urls)
fhandle = open('urls.txt','w')
for u in urls:
	fhandle.write(u)