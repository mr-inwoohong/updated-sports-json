import json
import requests
season = input('What year? ')
player_name = input('What player? ').title()

def nba_stats(player_name, season):
    url = f"https://www.balldontlie.io/api/v1/players?search={player_name}"
    response = requests.get(url)
    player_id = response.json()['data'][0]['id']

    url = f"https://www.balldontlie.io/api/v1/season_averages?player_ids[]={player_id}&season={season}"
    response = requests.get(url)
    data = response.json()['data'][0]
    player_stats = []
    stats = {
        "Player": player_name,
        "Season": data['season'],
        "Points per game": data['pts'],
        "FG %": data['fg_pct'],
        "FG3 %": data['fg3_pct'],
        "FT %": data['ft_pct'],
        "Rebounds per game": data['reb'],
        "Assists per game": data['ast'],
        "Steals per game": data['stl'],
        "Blocks per game": data['blk'],
        "Turnovers per game": data['turnover'],
        "FGM": data['fgm'],
        "FGA": data['fga'],
        "FG3M": data['fg3m'],
        "FG3A": data['fg3a'],
        "FTM": data['ftm'],
        "FTA": data['fta'],
        "OREB": data['oreb'],
        "DREB": data['dreb'],
    }
    player_stats.append(stats)
    return json.dumps(player_stats)

stats = nba_stats(f"{player_name}", f"{season}")
print(stats)
