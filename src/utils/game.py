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
    
    def getStreamingLink(self):
        home_team_name = self.home_performance.team.name
        abbrev_name_for_link = home_team_name.rsplit(' ', 1)[-1]
        return f"https://methstreams.com/nba-streams/{abbrev_name_for_link}/"