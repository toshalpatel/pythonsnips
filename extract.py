import tldextract

filename = "links_securityaffairs.txt"
fhandle = open(filename, "r")
domains = []


for line in fhandle:
	dom = tldextract.extract(line)
	if dom.domain != "wp":
		domains.append(dom.domain+'.'+dom.suffix)
fhandle.close()
domains = set(domains)
fhandle = open('domains.txt','w')
for d in domains:
	fhandle.write(d+'\n')
