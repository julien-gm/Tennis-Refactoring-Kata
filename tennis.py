# -*- coding: utf-8 -*-

class TennisGame:
    def __init__(self, player1Name, player2Name):
        self.p1N = player1Name
        self.p2N = player2Name
        self.p1points = 0
        self.p2points = 0
        
    def won_point(self, n):
        if n == self.p1N:
            self.p1points += 1
        else:
            self.p2points += 1
    
    def score(self):
        if (self.p1points < 4 and self.p2points < 4) and (self.p1points + self.p2points < 6):
            points = ["Love", "Fifteen", "Thirty", "Forty"]
            s = points[self.p1points]
            return s + "-All" if (self.p1points == self.p2points) else s + "-" + points[self.p2points]
        else:
            if (self.p1points == self.p2points):
                return "Deuce"
            s = self.p1N if self.p1points > self.p2points else self.p2N
            return "Advantage " + s if ((self.p1points-self.p2points)*(self.p1points-self.p2points) == 1) else "Win for " + s
