import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_810754.xml' 
fd = urllib.request.urlopen(url, context=ctx)
print('Retrieving', url)
data = fd.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data.decode())
results = tree.findall('comments/comment/count')
result = 0
for x in results:
	result += int(x.text)
print("Count:", len(results))
print("Sum:", result)
