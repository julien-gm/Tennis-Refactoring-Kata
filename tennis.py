# -*- coding: utf-8 -*-

all = "-All"
win = "Win for "
advantage = "Advantage "
deuce = "Deuce"
love = "Love"
fifteen = "Fifteen"
thirty = "Thirty"
forty = "Forty"

class TennisGame1:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1

        elif playerName == self.player2Name:
            self.p2points += 1

    def score(self):
        result = ""
        tempScore = 0
        if self.p1points == self.p2points:
            result = {
                0: love + all,
                1: fifteen + all,
                2: thirty + all,
            }.get(self.p1points, deuce)
        elif self.p1points >= 4 or self.p2points >= 4:
            minusResult = self.p1points - self.p2points
            if minusResult == 1:
                result = advantage + self.player1Name
            elif minusResult == -1:
                result = advantage + self.player2Name
            elif minusResult >= 2:
                result = win + self.player1Name
            else:
                result = win + self.player2Name
        else:
            for i in range(1, 3):
                if i == 1:
                    tempScore = self.p1points
                else:
                    result += "-"
                    tempScore = self.p2points
                result += {
                    0: love,
                    1: fifteen,
                    2: thirty,
                    3: forty,
                }[tempScore]
        return result


class TennisGame2:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.P1Score()
        elif playerName == self.player2Name:
            self.P2Score()

    def score(self):
        result = ""
        if self.p1points == self.p2points and self.p1points < 3:
            if self.p1points == 0:
                result = love
            elif self.p1points == 1:
                result = fifteen
            elif self.p1points == 2:
                result = thirty
            result += all
        if self.p1points == self.p2points and self.p1points > 2:
            result = deuce

        P1res = ""
        P2res = ""
        if self.p1points > 0 and self.p2points == 0:
            if self.p1points == 1:
                P1res = fifteen
            elif self.p1points == 2:
                P1res = thirty
            elif self.p1points == 3:
                P1res = forty

            P2res = love
            result = P1res + "-" + P2res
        if self.p2points > 0 and self.p1points == 0:
            if self.p2points == 1:
                P2res = fifteen
            elif self.p2points == 2:
                P2res = thirty
            elif self.p2points == 3:
                P2res = forty

            P1res = love
            result = P1res + "-" + P2res

        if self.p1points > self.p2points and self.p1points < 4:
            if self.p1points == 2:
                P1res = thirty
            elif self.p1points == 3:
                P1res = forty
            if self.p2points == 1:
                P2res = fifteen
            elif self.p2points == 2:
                P2res = thirty
            result = P1res + "-" + P2res
        if self.p2points > self.p1points and self.p2points < 4:
            if self.p2points == 2:
                P2res = thirty
            elif self.p2points == 3:
                P2res = forty
            if self.p1points == 1:
                P1res = fifteen
            elif self.p1points == 2:
                P1res = thirty
            result = P1res + "-" + P2res

        if self.p1points > self.p2points and self.p2points >= 3:
            result = advantage + self.player1Name

        if self.p2points > self.p1points and self.p1points >= 3:
            result = advantage + self.player2Name

        if (
            self.p1points >= 4
            and self.p2points >= 0
            and (self.p1points - self.p2points) >= 2
        ):
            result = win + self.player1Name
        if (
            self.p2points >= 4
            and self.p1points >= 0
            and (self.p2points - self.p1points) >= 2
        ):
            result = win + self.player2Name
        return result

    def SetP1Score(self, number):
        for i in range(number):
            self.P1Score()

    def SetP2Score(self, number):
        for i in range(number):
            self.P2Score()

    def P1Score(self):
        self.p1points += 1

    def P2Score(self):
        self.p2points += 1


class TennisGame3:
    def __init__(self, player1Name, player2Name):
        self.p1N = player1Name
        self.p2N = player2Name
        self.p1 = 0
        self.p2 = 0

    def won_point(self, n):
        if n == self.p1N:
            self.p1 += 1
        elif n == self.p2N:

            self.p2 += 1

    def score(self):
        if (self.p1 < 4 and self.p2 < 4) and (self.p1 + self.p2 < 6):
            p = [love, fifteen, thirty, forty]
            s = p[self.p1]
            return s + all if (self.p1 == self.p2) else s + "-" + p[self.p2]
        else:
            if self.p1 == self.p2:
                return deuce
            s = self.p1N if self.p1 > self.p2 else self.p2N
            return (
                advantage + s
                if ((self.p1 - self.p2) * (self.p1 - self.p2) == 1)
                else win + s
            )
