from boxsdk import OAuth2
import urllib2
import urlparse
import re
from boxsdk import Client
import sys


oauth = OAuth2(
    client_id='j2qt0drdofan7cln8iuqjrryue0rs9dw',
    client_secret='3SjQTFwTiT2tmh2McQ8j2vzawiC2SKRx',
    access_token = 'wezhFU1bx8UuBec4JZdWtvvNQ3WM6yhF',
    refresh_token = 'vLCckMNMbciiehup9cYGtlzKPWeJlHjuJdfUMe7QKDnf4EkstA6ZKSpqIoEiRHqh',
)

auth_url, csrf_token = oauth.get_authorization_url('https://www.getpostman.com/oauth2/callback')

if auth_url != '':
    print auth_url + '\n'
else:
    print 'null'

print csrf_token + '\n'

client = Client(oauth)

me = client.user(user_id='me').get()
print 'user_login: ' + me['login']

download_url = client.file(file_id='195695261746').get_shared_link_download_url()
print download_url

sys.exit(0)

parsed = urlparse.urlparse(auth_url)
params = dict(urlparse.parse_qsl(parsed.query))
auth_code = params['code']
print auth_code
csrf_state_token = re.findall('=([^&]+)',params['state'])
print csrf_state_token[0]

assert csrf_state_token[0] == csrf_token
access_token, refresh_token = oauth.authenticate(auth_code)




