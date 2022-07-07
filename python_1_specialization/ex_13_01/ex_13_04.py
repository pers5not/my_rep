import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

# http://py4e-data.dr-chuck.net/known_by_Fikret.html
# http://py4e-data.dr-chuck.net/known_by_Oriane.html

link = input("Enter URL - ")
pos = int(input("Enter position - ")) - 1
count = int(input("Enter count - ")) - 1


def url_ret(link, num):
    url = urllib.request.urlopen(f"{link}").read()
    soup = BeautifulSoup(url, 'html.parser')
    tags = soup('a')
    tag = tags[num].get('href')
    return tag


print(link)
for i in range(count):
    if link != url_ret(link, pos):
        link = url_ret(link, pos)
    print(url_ret(link, pos))
