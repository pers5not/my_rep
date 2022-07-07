from itertools import count
import json
import urllib.request
import urllib.parse
import urllib.error

# http://py4e-data.dr-chuck.net/comments_42.json
# http://py4e-data.dr-chuck.net/comments_1543583.json


url = urllib.request.urlopen(input("Enter location - "))
data = url.read().decode()

print('Retrieved', len(data), "characters")

try:
    js = json.loads(data)
except:
    js = None

counts = js["comments"]
print("Count:", len(counts))

Sum = 0

for item in counts:
    Sum = item["count"] + Sum

print("Sum:", Sum)
