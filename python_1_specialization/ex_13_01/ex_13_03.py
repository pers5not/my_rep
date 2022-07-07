import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup\

# http://py4e-data.dr-chuck.net/comments_1543580.html
url = urllib.request.urlopen(input("Enter URL - ")).read()

soup = BeautifulSoup(url, 'html.parser')

count = 0
Sum = 0

tags = soup(class_='comments')
for tag in tags:
    Sum = Sum + int(tag.text)
    count += 1

print(f"Count = {count}\nSum = {Sum}")
