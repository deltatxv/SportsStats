import datetime
import requests

from colorama import Style

from src.utils.tools import get_todays_games_json_from_url, get_games_from_json
from src.config import *

def printGame(game):
    home_team = game.home_performance.team.getFullName()
    home_score = game.home_performance.getPointsScored()

    away_team = game.away_performance.team.getFullName()
    away_score = game.away_performance.getPointsScored()

    time = game.getTime()
    
    if game.inProgress():
        print(f"{Fore.YELLOW}{time}:\t{OUTPUT_COLORS['AWAY']}{away_score} {OUTPUT_COLORS['@']}- {OUTPUT_COLORS['HOME']}{home_score}\t\t{OUTPUT_COLORS['AWAY']}{away_team} {OUTPUT_COLORS['@']}@ {OUTPUT_COLORS['HOME']}{home_team}")
        streaming_link = game.getStreamingLink()
        print(Style.RESET_ALL, f"-->Link: {streaming_link}")
    else:
        print(f"{Fore.YELLOW}{time}:\t{OUTPUT_COLORS['AWAY']}{away_team} {OUTPUT_COLORS['@']}@ {OUTPUT_COLORS['HOME']}{home_team}")

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
