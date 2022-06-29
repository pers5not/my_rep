from numpy import product
import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://patik.com.ua/g13607191-pobutova-himiya-dlya'

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"
}

response = requests.get(url, headers=headers)
src = response.text


def creating_soup(url):
    soup = BeautifulSoup(url, 'lxml')
    return soup


def get_all_group_links(url):
    all_groups_list = []
    group_hrefs = creating_soup(url).find_all(
        class_='b-product-groups-gallery__image-link')
    for href in group_hrefs:
        link = 'https://patik.com.ua/ua' + \
            href.get('href') + '?product_items_per_page=48'
        all_groups_list.append(link)
    return all_groups_list


def get_all_products_links(all_groups_list):
    all_products = []
    for group in all_groups_list:
        link_group = requests.get(group)
        products_hrefs = creating_soup(link_group.text).find_all(
            class_='b-product-gallery__image-link')
        for product in products_hrefs:
            all_products.append(product.get('href'))
    return all_products


count = 1
for prod in get_all_products_links(get_all_group_links(src)):
    print(prod, count)
    count += 1
