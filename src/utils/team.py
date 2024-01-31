class Team:
    def __init__(self, team_abbreviation, team_city, team_name):
        self.abbreviation = team_abbreviation
        self.city = team_city
        self.name = team_name

    def getFullName(self):
        return f"{self.city} {self.name}"