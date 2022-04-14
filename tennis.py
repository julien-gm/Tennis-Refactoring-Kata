

class TennisGame3:
    def __init__(self, player1Name, player2Name , player3Name):
        self.p1N = player1Name
        self.p2N = player2Name
        self.p3N = player3Name
        self.p1 = 0
        self.p2 = 0
        self.p3 = 0

    def won_point(self, n):
        if n == self.p1N:
            self.p1 += 1
        elif n == self.p2N: 
            self.p2 += 1
        else :
            self.p3 += 1

    def score(self):
        if (self.p1 < 4 and self.p2 < 4 and self.p3) and (self.p1 + self.p2 + self.p3 < 6):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            score = p[self.p1]
            return score + "-All" if (self.p1 == self.p2 or self.p1 == self.p3 or self.p2 == self.p3) else score + "-" + p[self.p2 , self.p3]
        else:
            if self.p1 == self.p2 or self.p1 == self.p3 or self.p2 == self.p3:
                return "Deuce"
            s = self.p1N if self.p1 > self.p2 or self.p1 > self.p3 or self.p2 > self.p3 else self.p2N
            return (
                "Advantage " + s
                if ((self.p1 - self.p2 - self.p3) * (self.p1 - self.p2 - self.p3) == 1)
                else "Win for " + s
            )

test = TennisGame3()
test()