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

        elif playerName == self.player2Name:
            self.p2points += 1

    def score(self):
        result = ""
        tempScore = 0
        if self.p1points == self.p2points:
            result = {
                0: LOVE + ALL,
                1: FIFTEEN + ALL,
                2: THIRTY + ALL,
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
            self.p1points += 1
        elif playerName == self.player2Name:
            self.p2points += 1

    def score(self):
        result = ""
        if self.p1points == self.p2points and self.p1points < 3:
            if self.p1points == 0:
                result = LOVE
            elif self.p1points == 1:
                result = FIFTEEN
            elif self.p1points == 2:
                result = THIRTY
            result += ALL
        if self.p1points == self.p2points and self.p1points > 2:
            result = DEUCE

        P1res = ""
        P2res = ""
        if self.p1points > 0 and self.p2points == 0:
            if self.p1points == 1:

                P1res = FIFTEEN
            elif self.p1points == 2:
                P1res = THIRTY
            elif self.p1points == 3:
                P1res = FORTY

            P2res = LOVE
            result = P1res + "-" + P2res
        if self.p2points > 0 and self.p1points == 0:
            if self.p2points == 1:

                P2res = FIFTEEN
            elif self.p2points == 2:
                P2res = THIRTY
            elif self.p2points == 3:
                P2res = FORTY

            P1res = LOVE
            result = P1res + "-" + P2res

        if self.p1points > self.p2points and self.p1points < 4:
            if self.p1points == 2:
                P1res = THIRTY
            elif self.p1points == 3:
                P1res = FORTY
            if self.p2points == 1:
                P2res = FIFTEEN
            elif self.p2points == 2:
                P2res = THIRTY
            result = P1res + "-" + P2res
        if self.p2points > self.p1points and self.p2points < 4:
            if self.p2points == 2:
                P2res = THIRTY
            elif self.p2points == 3:
                P2res = FORTY
            if self.p1points == 1:
                P1res = FIFTEEN
            elif self.p1points == 2:
                P1res = THIRTY

            result = P1res + "-" + P2res

        if self.p1points > self.p2points and self.p2points >= 3:
            result = ADVANTAGE + self.player1Name

        if self.p2points > self.p1points and self.p1points >= 3:
            result = ADVANTAGE + self.player2Name

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


class TennisGame3:
    def __init__(self, player1Name, player2Name):
        self.name_player_1 = player1Name
        self.name_player_2 = player2Name
        self.score_player_1 = 0
        self.score_player_2 = 0

    def won_point(self, n):
        if n == self.name_player_1:
            self.score_player_1 += 1
        elif n == self.name_player_2:
            self.score_player_2 += 1

    def score(self):
        if (self.score_player_1 < 4 and self.score_player_2 < 4) and (
            self.score_player_1 + self.score_player_2 < 6
        ):
            point = [LOVE, FIFTEEN, THIRTY, FORTY]
            score = p[self.score_player_1]
            if self.score_player_1 == self.score_player_2:
                return score + ALL
            else:
                return score + "-" + point[self.score_player_2]
        else:

            if self.score_player_1 == self.score_player_2:
                return DEUCE

            if self.score_player_1 > self.score_player_2:
                win_player = self.name_player_1
            elif self.score_player_1 < self.score_player_2:
                win_player = self.name_player_2

            if abs(self.score_player_1 - self.score_player_2)  == 1:
                return ADVANTAGE + win_player
            else:
                return WIN + win_player
