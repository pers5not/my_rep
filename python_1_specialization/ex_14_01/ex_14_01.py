import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET

# http://py4e-data.dr-chuck.net/comments_42.xml
# http://py4e-data.dr-chuck.net/comments_1543582.xml
data = input('Enter location - ')

xml_data = urllib.request.urlopen(data).read()

lst = ET.fromstring(xml_data)
counts = lst.findall('.//count')
Sum = 0
print('Count:', len(counts))

for item in counts:
    Sum = int(item.text) + Sum

print('Sum:', Sum)
