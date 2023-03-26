import requests
from bs4 import BeautifulSoup
import json

import lxml

search = input('Who are you looking for?')
search = search.replace(' ', '')

url = f'https://news.google.com/rss/search?q={search}'

def headline(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="xml")

    results = soup.find_all('item')
    link = soup.find('link')
    print(results)

    productslist = []
    for item in results:
        product = {
            'title': item.find('title').text,
            'link': item.find('link').text,
        }
        productslist.append(product)
    return json.dumps(productslist)

headline(url)

