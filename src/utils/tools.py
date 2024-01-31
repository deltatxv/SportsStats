import requests

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
'''
{
    - team abbrev
    - team city
    - team name
    - full name = name + city
    - q1 score
    - q2 score
    - q3 score
    - q4 score
    - total score
}
'''

def get_games_from_json(input_list):
    games = []
    for game in input_list:
        home = game.get('h')
        away = game.get('v')
        time = game.get('stt')
        
        home_team = home.get('tc') + ' ' + home.get('tn')
        away_team = away.get('tc') + ' ' + away.get('tn')
        
        home_score = home.get('s')
        away_score = away.get('s')
        
        games.append([home_team, away_team, time, home_score, away_score])
    return games

# def get_streaming_link_for_game(game):
#     # TODO: make mapping for correct team names "Golden State Warriors" doesnt work"
#     home_team = game[0]
#     return f"https://methstreams.com/nba-streams/{home_team}/"