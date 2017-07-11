import re
import urllib2
import urlparse

auth_url = 'http://0.0.0.0/?state=security_token%3DKnhMJatFipTAnM0nHlZA&code=N81rSvxhbXDe94oo0IS3e38tfDr2IRdP'

parsed = urlparse.urlparse(auth_url)
params = dict(urlparse.parse_qsl(parsed.query))
auth_code = params['code']
print auth_code
csrf_state_token = re.findall('=([^&]+)',params['state'])
print csrf_state_token[0]
