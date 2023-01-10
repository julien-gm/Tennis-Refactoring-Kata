# -*- coding: utf-8 -*-


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
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.p1points, "Deuce")
        elif self.p1points >= 4 or self.p2points >= 4:
            minusResult = self.p1points - self.p2points
            if minusResult == 1:
                result = "Advantage " + self.player1Name
            elif minusResult == -1:
                result = "Advantage " + self.player2Name
            elif minusResult >= 2:
                result = "Win for " + self.player1Name
            else:
                result = "Win for " + self.player2Name
        else:
            for i in range(1, 3):
                if i == 1:
                    tempScore = self.p1points
                else:
                    result += "-"
                    tempScore = self.p2points
                result += {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty",
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
                result = "Love"
            if self.p1points == 1:
                result = "Fifteen"
            if self.p1points == 2:
                result = "Thirty"
            result += "-All"
        if self.p1points == self.p2points and self.p1points > 2:
            result = "Deuce"

        P1res = ""
        P2res = ""
        if self.p1points > 0 and self.p2points == 0:
            if self.p1points == 1:
                P1res = "Fifteen"
            if self.p1points == 2:
                P1res = "Thirty"
            if self.p1points == 3:
                P1res = "Forty"

            P2res = "Love"
            result = P1res + "-" + P2res
        if self.p2points > 0 and self.p1points == 0:
            if self.p2points == 1:
                P2res = "Fifteen"
            if self.p2points == 2:
                P2res = "Thirty"
            if self.p2points == 3:
                P2res = "Forty"

            P1res = "Love"
            result = P1res + "-" + P2res

        if self.p1points > self.p2points and self.p1points < 4:
            if self.p1points == 2:
                P1res = "Thirty"
            if self.p1points == 3:
                P1res = "Forty"
            if self.p2points == 1:
                P2res = "Fifteen"
            if self.p2points == 2:
                P2res = "Thirty"
            result = P1res + "-" + P2res
        if self.p2points > self.p1points and self.p2points < 4:
            if self.p2points == 2:
                P2res = "Thirty"
            if self.p2points == 3:
                P2res = "Forty"
            if self.p1points == 1:
                P1res = "Fifteen"
            if self.p1points == 2:
                P1res = "Thirty"
            result = P1res + "-" + P2res

        if self.p1points > self.p2points and self.p2points >= 3:
            result = "Advantage " + self.player1Name

        if self.p2points > self.p1points and self.p1points >= 3:
            result = "Advantage " + self.player2Name

        if (
            self.p1points >= 4
            and self.p2points >= 0
            and (self.p1points - self.p2points) >= 2
        ):
            result = "Win for " + self.player1Name
        if (
            self.p2points >= 4
            and self.p1points >= 0
            and (self.p2points - self.p1points) >= 2
        ):
            result = "Win for " + self.player2Name
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
        self.name_player_1 = player1Name
        self.name_player_2 = player2Name
        self.score_player_1 = 0
        self.score_player_2 = 0

    def won_point(self, name):
        if name == self.name_player_1:
            self.score_player_1 += 1
        elif name == self.name_player_2:
            self.score_player_2 += 1

    def score(self):
        if (self.score_player_1 < 4 and self.score_player_2 < 4) and (self.score_player_1 + self.score_player_2 < 6):
            point = ["Love", "Fifteen", "Thirty", "Forty"]
            real_score = point[self.score_player_1]
            if (self.score_player_1 == self.score_player_2):
                return real_score + "-All" 
            else :
                return real_score + "-" + point[self.score_player_2]
        else:
            
            if self.score_player_1 == self.score_player_2:
                return "Deuce"
            
            if self.score_player_1 > self.score_player_2 :
                win_player = self.name_player_1  
            else:
                win_player = self.name_player_2
            
            if abs(self.score_player_1 - self.score_player_2)  == 1:
                return "Advantage " + win_player
            else :
                return  "Win for " + win_player
            
