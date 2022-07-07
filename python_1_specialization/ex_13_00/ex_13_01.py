from os import link
import urllib.request
import urllib.parse
import urllib.error
import re

fhand = urllib.request.urlopen('https://regionbud.com.ua')

for line in fhand:
    link_line = re.search(
        "^<a href=\"https:([a-zA-Z0-9-./]*)", line.decode().strip())
    if link_line == None or "/index.php" in link_line[0]:
        continue
    if "<a href=\"https://" in link_line[0]:
        new_link_line = link_line[0].replace("<a href=\"", "")
        print(new_link_line)
