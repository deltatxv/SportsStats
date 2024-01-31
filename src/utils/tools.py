import requests

from src.utils.game import Game
from src.utils.teamPerformance import TeamPerformance
from src.utils.team import Team

games_header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/57.0.2987.133 Safari/537.36',
    'Dnt': '1',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en',
    'origin': 'http://stats.nba.com',
    'Referer': 'https://github.com'
}

def get_todays_games_json_from_url(url):
    raw_data = requests.get(url, headers=games_header)
    json = raw_data.json()
    return json.get('gs').get('g')

def get_team_performance_from_json(team_json):
    team = Team(team_json.get('ta'), team_json.get('tc'), team_json.get('tn'))
    team_performance = TeamPerformance(team)
    # TODO: add overtime
    for i in range(4):
        team_performance.addPoints(0, int(team_json.get(f'q{i+1}')))
    return team_performance
    
def get_games_from_json(input_list):
    games = []
    for game in input_list:
        home_json = game.get('h')
        home_team_performance = get_team_performance_from_json(home_json)

        away_json = game.get('v')
        away_team_performance = get_team_performance_from_json(away_json)

        time = game.get('stt')
        game = Game(home_team_performance, away_team_performance, time)
        games.append(game)

    return games