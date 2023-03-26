import requests
from bs4 import BeautifulSoup
import json

player_name = input("What pitcher? ")

player_first_name, player_last_name = player_name.split(" ")
player_first_name = player_first_name.lower()
player_last_name = player_last_name.lower().replace(" ", "_")

url = f"https://www.baseball-reference.com/players/{player_last_name[0]}/{player_last_name[0:5]}{player_first_name[0:2]}01.shtml"
print(url)

def mlb_pitching_stats(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', {'id': 'pitching_standard'})

    data_rows = table.find('tbody').find_all('tr')

    data = []
    for row in data_rows:
        cols = row.find_all(['th', 'td'])
            cols = [col.text.strip() for col in cols]
        data.append(cols)

    return json.dumps(data)


stats = mlb_pitching_stats(url)
print(stats)