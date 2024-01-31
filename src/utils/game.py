import time
import re

class Game:
    def __init__(self, home_team_performance, away_team_performance, game_time):
        self.home_performance = home_team_performance
        self.away_performance = away_team_performance
        self.time = game_time

    def inProgress(self):
        if "ET" in self.time or "Final" in self.time:
            return False
        else:
            return True

    def getTime(self):
        if self.inProgress():
            return self.time

        # Parse time string (e.g. "7:00 pm ET") to PT
        match = re.match(r'(\d+):(\d+) ([apmAPM]+) (\w+)', self.time)
        if match:
            hours, minutes, am_pm, timezone = match.groups()

            hours = int(hours)
            hours -= 3 # 3 hour time diff from est to pst
            return f"{str(hours)}:{minutes}"
        else:
            # default to whatever nba api gave us
            return self.time

    def getStreamingLink(self):
        home_team_name = self.home_performance.team.name
        abbrev_name_for_link = home_team_name.rsplit(' ', 1)[-1]
        return f"https://methstreams.com/nba-streams/{abbrev_name_for_link}/"