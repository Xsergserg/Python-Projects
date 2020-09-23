from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
if len(url) == 0:
	url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
count = input("Enter count: ")
pos = input("Enter position: ")
count = int(count)
pos = int(pos)
i = 0

print("Retrieving:", url)
while i < count:
	html = urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, "html.parser")
	tags = soup('a')
	line = tags[pos - 1]
	url = re.findall('<a href="(.*)"', str(tags[pos - 1]))[0]
	print("Retrieving:", url)
	i += 1
print ("Answer:", re.findall(r'.*by_(.*)\.', url)[0])
