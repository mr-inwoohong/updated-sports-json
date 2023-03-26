import pandas as pd
from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError
import pprint
import json


APPLICATION_ID = 'ianhong-weezy-PRD-bbfa4472b-704c86fb'
search = input('What item are you looking for?')
savesearch = search.replace(' ', '')

def get_results(search):
    api = Finding(appid= APPLICATION_ID, config_file=None)
    response = api.execute('findItemsAdvanced', {'keywords': f"{search}"})
    info = response.dict()
    results = info['searchResult']
    items = results['item']


    productslist = []
        # watch = items['listingInfo']['watchCount']
        # print(watch)
    for i in items:
        product = {
            'title': i['title'],
            'price/bid': i['sellingStatus']['convertedCurrentPrice']['value'],
            'listing_type': i['listingInfo']['listingType'],
            'buy_now_available': i['listingInfo']['buyItNowAvailable'],
            'location': i['location'],
            'url': i['viewItemURL'],
            'picture': i['galleryURL'],
            'end_time': i['listingInfo']['endTime'],
            #'watch_count': i['listingInfo']['watchCount'],
        }

        productslist.append(product)
        return json.dumps(productslist)
        #print(productslist1)
        #data = pd.DataFrame(productslist)
        #data.to_csv(f"data/current{savesearch}.csv", index=False)

        #print(items[0])


results = get_results(f'{search}')
print(results)