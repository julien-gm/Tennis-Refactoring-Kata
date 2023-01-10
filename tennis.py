# -*- coding: utf-8 -*-

ADVANTAGE = "Advantage "
WIN = "Win for "
LOVE = "Love"
FIFTEEN = "Fifteen"
THIRTY = "Thirty"
FORTY = "Forty"
DEUCE = "Deuce"
ALL = "-All"


class TennisGame1:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        result = ""
        tempScore = 0
        if self.p1points == self.p2points:
            result = {
                0: "LOVE-ALL",
                1: "FIFTEEN-ALL",
                2: "THIRTY-ALL",
            }.get(self.p1points, DEUCE)
        elif self.p1points >= 4 or self.p2points >= 4:
            minusResult = self.p1points - self.p2points
            if minusResult == 1:
                result = ADVANTAGE + self.player1Name
            elif minusResult == -1:
                result = ADVANTAGE + self.player2Name
            elif minusResult >= 2:
                result = WIN + self.player1Name
            else:
                result = WIN + self.player2Name
        else:
            for i in range(1, 3):
                if i == 1:
                    tempScore = self.p1points
                else:
                    result += "-"
                    tempScore = self.p2points
                result += {
                    0: LOVE,
                    1: FIFTEEN,
                    2: THIRTY,
                    3: FORTY,
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
        else:
            self.P2Score()

    def score(self):
        result = ""
        if self.p1points == self.p2points and self.p1points < 3:
            if self.p1points == 0:
                result = LOVE
            if self.p1points == 1:
                result = FIFTEEN
            if self.p1points == 2:
                result = THIRTY
            result += ALL
        if self.p1points == self.p2points and self.p1points > 2:
            result = DEUCE

        P1res = ""
        P2res = ""
        if self.p1points > 0 and self.p2points == 0:
            if self.p1points == 1:
                P1res = FIFTEEN
            if self.p1points == 2:
                P1res = THIRTY
            if self.p1points == 3:
                P1res = FORTY

            P2res = LOVE
            result = P1res + "-" + P2res
        if self.p2points > 0 and self.p1points == 0:
            if self.p2points == 1:
                P2res = FIFTEEN
            if self.p2points == 2:
                P2res = THIRTY
            if self.p2points == 3:
                P2res = FORTY

            P1res = LOVE
            result = P1res + "-" + P2res

        if self.p1points > self.p2points and self.p1points < 4:
            if self.p1points == 2:
                P1res = THIRTY
            if self.p1points == 3:
                P1res = FORTY
            if self.p2points == 1:
                P2res = FIFTEEN
            if self.p2points == 2:
                P2res = THIRTY
            result = P1res + "-" + P2res
        if self.p2points > self.p1points and self.p2points < 4:
            if self.p2points == 2:
                P2res = THIRTY
            if self.p2points == 3:
                P2res = FORTY
            if self.p1points == 1:
                P1res = FIFTEEN
            if self.p1points == 2:
                P1res = THIRTY
            result = P1res + "-" + P2res

        if self.p1points > self.p2points and self.p2points >= 3:
            result = "a " + self.player1Name

        if self.p2points > self.p1points and self.p1points >= 3:
            result = "a " + self.player2Name

        if (
            self.p1points >= 4
            and self.p2points >= 0
            and (self.p1points - self.p2points) >= 2
        ):
            result = WIN + self.player1Name
        if (
            self.p2points >= 4
            and self.p1points >= 0
            and (self.p2points - self.p1points) >= 2
        ):
            result = WIN + self.player2Name
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
        else:
            self.p2 += 1

    def score(self):
        if (self.p1 < 4 and self.p2 < 4) and (self.p1 + self.p2 < 6):
            p = [LOVE, FIFTEEN, THIRTY, FORTY]
            s = p[self.p1]
            return s + ALL if (self.p1 == self.p2) else s + "-" + p[self.p2]
        else:
            if self.p1 == self.p2:
                return DEUCE
            s = self.p1N if self.p1 > self.p2 else self.p2N
            return (
                ADVANTAGE + s
                if ((self.p1 - self.p2) * (self.p1 - self.p2) == 1)
                else WIN + s
            )
