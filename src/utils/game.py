import re

def convert_et_time_string_to_pacific(et_time_str):
    # Parse time string (e.g. "7:00 pm ET") to PT
    match = re.match(r'(\d+):(\d+) ([apmAPM]+) (\w+)', et_time_str)
    if match:
        hours, minutes, am_pm, timezone = match.groups()

        hours = int(hours)
        hours -= 3 # 3 hour time diff from est to pst
        return f"{str(hours)}:{minutes}"
    else:
        # default to whatever we were given
        return et_time_str

class Game:
    def __init__(self, game_id, home_team_performance, away_team_performance, game_time):
        self.game_id = game_id
        self.home_performance = home_team_performance
        self.away_performance = away_team_performance
        self.time = game_time

    def inProgress(self):
        if (self.isFinished() is False) and ("ET" not in self.time):
            return True
        else:
            return False
    
    def isFinished(self):
        return "Final" in self.time

    def getTime(self):
        if self.inProgress():
            return self.time
        else:
            return convert_et_time_string_to_pacific(self.time)

    def getStreamingLink(self):
        home_team_name = self.home_performance.team.name
        abbrev_name_for_link = home_team_name.rsplit(' ', 1)[-1]
        return f"https://methstreams.com/nba-streams/{abbrev_name_for_link}/"