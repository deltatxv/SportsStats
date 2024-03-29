from colorama import Style

from src.utils.tools import get_todays_games_json_from_url, get_games_from_json
from src.config import *

def printGame(game):
    home_team = game.home_performance.team.getFullName()
    home_score = game.home_performance.getPointsScored()

    away_team = game.away_performance.team.getFullName()
    away_score = game.away_performance.getPointsScored()

    time = game.getTime()
    if game.isFinished():
        print(f"{Fore.YELLOW}{time}:\t{OUTPUT_COLORS['AWAY']}{away_score} {OUTPUT_COLORS['@']}- {OUTPUT_COLORS['HOME']}{home_score}\t\t{OUTPUT_COLORS['AWAY']}{away_team} {OUTPUT_COLORS['@']}@ {OUTPUT_COLORS['HOME']}{home_team}")
    elif game.inProgress():
        print(f"{Fore.YELLOW}{time}:\t{OUTPUT_COLORS['AWAY']}{away_score} {OUTPUT_COLORS['@']}- {OUTPUT_COLORS['HOME']}{home_score}\t\t{OUTPUT_COLORS['AWAY']}{away_team} {OUTPUT_COLORS['@']}@ {OUTPUT_COLORS['HOME']}{home_team}")
        streaming_link = game.getStreamingLink()
        print(Style.RESET_ALL, f"-->Link: {streaming_link}") 
    else:
        print(f"{Fore.YELLOW}{time}:\t{OUTPUT_COLORS['AWAY']}{away_team} {OUTPUT_COLORS['@']}@ {OUTPUT_COLORS['HOME']}{home_team}")

    # TODO: improve this to pretty print
    # box_score_df = get_box_score(game.game_id)
    # print(box_score_df)

def printGames(games):
    for game in games:
        printGame(game)

def printTodaysGames():
    data = get_todays_games_json_from_url(TODAYS_GAMES_URL)
    games = get_games_from_json(data)
    # for debugging, uncomment next line
    # print(data)
    printGames(games)
