import datetime
import requests

from src.utils.tools import *
from src.config import *

def printGame(game):
    home_team = game[0]
    away_team = game[1]
    time = game[2]
    
    if "EST" not in time: # means already started (i.e. Q1, Final, etc.)
        home_score = game[3]
        away_score = game[4]
        
    print(f"{Fore.YELLOW}{time}:\t\t{OUTPUT_COLORS['AWAY']}{away_score} {OUTPUT_COLORS['@']}- {OUTPUT_COLORS['HOME']}{home_score}\t\t{OUTPUT_COLORS['AWAY']}{away_team} {OUTPUT_COLORS['@']}@ {OUTPUT_COLORS['HOME']}{home_team}")
    
def printGames(games):
    for game in games:
        printGame(game)

def printTodaysGames():
    data = get_todays_games_json_from_url(TODAYS_GAMES_URL)
    games = get_games_from_json(data)
    # print(data)
    print(f"{OUTPUT_COLORS['HEADER']}There are {len(games)} games scheduled for today:\n")
    printGames(games)
    print()
