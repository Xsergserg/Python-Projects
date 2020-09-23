import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_810755.json'
fd = urllib.request.urlopen(url)
print('Retrieving', url)
data = fd.read()
print('Retrieved', len(data), 'characters')
info = json.loads(data)["comments"]
print('Count:', len(info))
sum = 0
for item in info:
	sum += int(item["count"])
print('Sum:', sum)
