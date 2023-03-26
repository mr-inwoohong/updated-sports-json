import json
import requests
from bs4 import BeautifulSoup

player_name = input("What player? ")

#currently year not working
#year = input("what year?")
#url = f"https://www.baseball-reference.com/players/gl.fcgi?id={player_last_name[0]}/{player_last_name}{player_first_name[0:2]}01&t=b&year={year}"
#table = soup.find('table', {'id': 'batting_gamelogs'})

player_first_name, player_last_name = player_name.split(" ")
player_first_name = player_first_name.lower()
player_last_name = player_last_name.lower().replace(" ", "_")

url = f"https://www.baseball-reference.com/players/{player_last_name[0]}/{player_last_name[0:5]}{player_first_name[0:2]}01.shtml"

print(url)


def mlb_batting_stats(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', {'id': 'batting_standard'})

    data_rows = table.find('tbody').find_all('tr')

    data = []

    data_dict = {}
    for row in data_rows:
        cols = row.find_all(['th', 'td'])
        cols = [col.text.strip() for col in cols]
        key = cols[0]  # assuming the key is in the first column
        data_dict[key] = [{'Year': cols[1], 'Age': cols[2], 'League': cols[3], 'Games Played': cols[4], 'Plate Appearance': cols[5], 'At Bat': cols[6], 'Runs Scored': cols[7], 'Hits': cols[8], 'Doubles': cols[9], 'Triples': cols[10], 'Homeruns': cols[11], 'RBI': cols[12], 'Stolen Bases': cols[13], 'Caught Stealing': cols[14], 'BB/Walks': cols[15], 'Strikeouts': cols[16], 'At Bats': cols[17], 'OBP': cols[18], 'SLG': cols[19], 'OPS': cols[20], 'OPS+': cols[21]}]


    # for row in data_rows:
    #     cols = row.find_all(['th', 'td'])
    #     cols = [col.text.strip() for col in cols]
    #
    #     data.append(cols)

    return json.dumps(data_dict)


stats = mlb_batting_stats(url)
print(stats)