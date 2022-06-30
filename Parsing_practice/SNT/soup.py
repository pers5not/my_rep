from bs4 import BeautifulSoup


def creating_soup(url):
    soup = BeautifulSoup(url, 'lxml')
    return soup
