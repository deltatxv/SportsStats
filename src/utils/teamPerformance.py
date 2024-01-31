class TeamPerformance:
    def __init__(self, team):
        self.team = team
        self.scores_by_period = [] # q1, q2, q3, q4, ot1, etc.

    def addPoints(self, period, score):
        self.scores_by_period.insert(period, score)
        
    def getPointsScored(self):
        total_score = 0
        for score in self.scores_by_period:
            total_score += int(score)
        return total_score