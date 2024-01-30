from colorama import Fore

TODAYS_GAMES_URL = 'https://data.nba.com/data/10s/v2015/json/mobile_teams/nba/2023/scores/00_todays_scores.json'

OUTPUT_COLORS = {
    "HOME" : Fore.GREEN,
    "AWAY" : Fore.BLUE,
    "@" : Fore.WHITE,
    "HEADER" : Fore.YELLOW
}