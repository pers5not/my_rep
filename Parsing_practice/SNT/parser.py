from bs4 import BeautifulSoup
import csv
import re
import requests
from collections import OrderedDict
from soup import creating_soup as soup

url = 'http://snt.od.ua/stekljannaja-posuda'

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"
}

response = requests.get(url, headers=headers)
src = response.text


def all_links_list(url):
    group_list = []
    hrefs_group = soup(url).find_all('tr')
    for href in hrefs_group:
        td_group = href.find_all('td')
        for link in td_group:
            link_group = link.find('a')
            if link_group != None:
                group_list.append(link_group.get('href'))
    group_list = list(OrderedDict.fromkeys(group_list))
    return group_list


for i in all_links_list(src):
    print(i)
