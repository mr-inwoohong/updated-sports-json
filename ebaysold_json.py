import requests
from bs4 import BeautifulSoup
import json
from csv import reader


searchterm = input("What sold item are you looking for?")
savesearch = searchterm.replace(' ', '')
url = f'https://www.ebay.com/sch/i.html?_from=R40&_nkw={searchterm}&_sacat=0&LH_PrefLoc=1&LH_Auction=1&rt=nc&LH_Sold=1&LH_Complete=1'


def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    productslist = []
    results = soup.find_all('div', {'class': 's-item__info clearfix'})

    solddate = soup.find('div', class_='s-item__title--tagblock')
    #bids = soup.find('span', class_= 's-item__bids s-item__bidCount').text
    for item in results:
        product = {
            'title': item.find('div', {'class': 's-item__title'}).text,
            'soldprice': float(item.find('span', {'class': 's-item__price'}).text.replace('$','').replace(',','').strip()),
            'solddate': solddate.find('span', {'class': 'POSITIVE'}).text,
            #'bids': bids,
            'link': item.find('a', {'class': 's-item__link'})['href'],
        }
        productslist.append(product)
    return json.dumps(productslist)

stats = get_data(url)
print(stats)





