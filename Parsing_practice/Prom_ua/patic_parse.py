import requests
from bs4 import BeautifulSoup
import csv
import re

response = requests.get('https://patik.com.ua/g13429262-zasobi-dlya-prannya')


def soup(obj):
    soup = BeautifulSoup(obj, 'lxml')
    return soup


def get_list_links(url):
    list_html = []
    group_hrefs = soup(url.text).find_all(
        class_='b-product-groups-gallery__image-link')
    for href in group_hrefs:
        link = href.get('href').replace('/', '')
        list_html.append(link)
    return list_html


def downoald_html(list_links):
    for link in list_links:
        response = requests.get(
            'https://patik.com.ua/ua/' + link + '?product_items_per_page=48')
        f = open(f"{link}.html", 'w')
        f.write(response.text)
    f.close


def open_html(pages_html):
    all_products = []
    for page in pages_html:
        if 'uag' in page:
            page = page.replace('uag', 'g')
        f = open(page + '.html')
        products_hrefs = soup(f).find_all(
            class_='b-product-gallery__image-link')
        for product in products_hrefs:
            all_products.append(product.get('href'))
    f.close()
    return all_products


open_html(get_list_links(response))
