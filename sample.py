import tldextract
import re

link = 'h t t p : / / f o r u m s . n e w s . c n n . c o m /'
url = re.sub(r"\s","",link)
print(url)
subb = tldextract.extract(url)
print(subb.domain+'.'+subb.suffix)