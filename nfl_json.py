import requests
from bs4 import BeautifulSoup
import pandas as pd
import json


year = input('What year?')
player_name = input('What player?').title().replace('*', '', 1).replace('+', '', 1)
football_url = f'https://www.pro-football-reference.com/years/{year}/fantasy.htm'
savesearch = player_name.replace(' ', '')


def nfl_stats(football_url):
    # Send a GET request to the URL

    r = requests.get(football_url)

    # Check if the request was successful
    if r.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(r.text, 'html.parser')
        #productslist = []

        # Find the element containing the data you want to scrape

        # Extract the data from the element
        headers = [th.getText() for th in soup.findAll('tr')[1].findAll('th')]
        headers = headers[1:]
        rows = soup.findAll('tr', class_=lambda table_rows: table_rows != "thead")
        player_stats = [[td.getText() for td in rows[i].findAll('td')]
                        for i in range(len(rows))]
        player_stats = player_stats[2:]
        stats = pd.DataFrame(player_stats, columns=headers)
        player = stats['Player'].str.contains(f'{player_name}')
        data = pd.DataFrame(stats[player])
        data_dict = data.to_dict(orient='records')
        json_data = json.dumps(data_dict)
        # Return the data
        return json_data
    else:
        # If the request failed, return None
        return None

data = nfl_stats(football_url)
if data is not None:
    print("Scraped data:", data)
else:
    print("Failed to scrape data.")






# r = requests.get(football_url)
# soup = BeautifulSoup(r.text, 'html.parser')
# productslist = []
# headers = [th.getText() for th in soup.findAll('tr')[1].findAll('th')]
# headers = headers[1:]
# rows = soup.findAll('tr', class_=lambda table_rows: table_rows != "thead")
# player_stats = [[td.getText() for td in rows[i].findAll('td')]
#                 for i in range(len(rows))]
# player_stats = player_stats[2:]
# stats = pd.DataFrame(player_stats, columns=headers)
#
# player = stats['Player'].str.contains(f'{player_name}')
# data = pd.DataFrame(stats[player])
# print(data)
# data.to_csv(f"data/stats{savesearch}.csv", index=False)

#json_data = data.to_json()
