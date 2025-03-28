# -*- coding: utf-8 -*-
from player_class import Player


ADVANTAGE = "Advantage "
WIN = "Win for "
LOVE = "Love"
FIFTEEN = "Fifteen"
THIRTY = "Thirty"
FORTY = "Forty"
DEUCE = "Deuce"
ALL = "-All"


class TennisGame1:
    def __init__(self, player1, player2):
        self.player1 = Player(player1)
        self.player2 = Player(player2)
        self.game_over = False

    def won_point(self, playerName):
        if self.game_over:
            raise Exception("Game is over")
        if playerName == self.player1.name:
            self.player1.points += 1
        elif playerName == self.player2.name:
            self.player2.points += 1

    def score(self):
        result = ""
        tempScore = 0
        if self.player1.points == self.player2.points:
            result = {
                0: LOVE + ALL,
                1: FIFTEEN + ALL,
                2: THIRTY + ALL,
            }.get(self.player1.points, DEUCE)
        elif self.player1.points >= 4 or self.player2.points >= 4:
            minusResult = self.player1.points - self.player2.points
            if minusResult == 1:
                result = ADVANTAGE + self.player1.name
            elif minusResult == -1:
                result = ADVANTAGE + self.player2.name
            elif minusResult >= 2:
                result = WIN + self.player1.name
                self.game_over = True
            else:
                result = WIN + self.player2.name
                self.game_over = True
        else:
            for i in range(1, 3):
                if i == 1:
                    tempScore = self.player1.points
                else:
                    result += "-"
                    tempScore = self.player2.points
                result += {
                    0: LOVE,
                    1: FIFTEEN,
                    2: THIRTY,
                    3: FORTY,
                }[tempScore]
        return result


class TennisGame2:
    def __init__(self, player1, player2):
        self.p1 = Player(player1)
        self.p2 = Player(player2)

    def won_point(self, player):
        if player == self.p1.name:
            self.p1.points += 1
        elif player == self.p2.name:
            self.p2.points += 1

    def score(self):
        result = ""
        if self.p1.points == self.p2.points and self.p1.points < 3:
            if self.p1.points == 0:
                result = LOVE
            elif self.p1.points == 1:
                result = FIFTEEN
            elif self.p1.points == 2:
                result = THIRTY
            result += ALL
        if self.p1.points == self.p2.points and self.p1.points > 2:
            result = DEUCE

        P1res = ""
        P2res = ""
        if self.p1.points > 0 and self.p2.points == 0:
            if self.p1.points == 1:
                P1res = FIFTEEN
            elif self.p1.points == 2:
                P1res = THIRTY
            elif self.p1.points == 3:
                P1res = FORTY

            P2res = LOVE
            result = P1res + "-" + P2res
        if self.p2.points > 0 and self.p1.points == 0:
            if self.p2.points == 1:
                P2res = FIFTEEN
            elif self.p2.points == 2:
                P2res = THIRTY
            elif self.p2.points == 3:
                P2res = FORTY
            P1res = LOVE
            result = P1res + "-" + P2res

        if self.p1.points > self.p2.points and self.p1.points < 4:
            if self.p1.points == 2:
                P1res = THIRTY
            elif self.p1.points == 3:
                P1res = FORTY
            if self.p2.points == 1:
                P2res = FIFTEEN
            elif self.p2.points == 2:
                P2res = THIRTY
            result = P1res + "-" + P2res
        if self.p2.points > self.p1.points and self.p2.points < 4:
            if self.p2.points == 2:
                P2res = THIRTY
            elif self.p2.points == 3:
                P2res = FORTY
            if self.p1.points == 1:
                P1res = FIFTEEN
            elif self.p1.points == 2:
                P1res = THIRTY
            result = P1res + "-" + P2res

        if self.p1.points > self.p2.points and self.p2.points >= 3:
            result = ADVANTAGE + self.p1.name

        if self.p2.points > self.p1.points and self.p1.points >= 3:
            result = ADVANTAGE + self.p2.name

        if (
            self.p1.points >= 4
            and self.p2.points >= 0
            and (self.p1.points - self.p2.points) >= 2
        ):
            result = WIN + self.p1.name
        if (
            self.p2.points >= 4
            and self.p1.points >= 0
            and (self.p2.points - self.p1.points) >= 2
        ):
            result = WIN + self.p2.name
        return result


class TennisGame3:
    def __init__(self, player1_name, player2_name):
        self.p1 = Player(player1_name)
        self.p2 = Player(player2_name)

    def won_point(self, name):
        if name == self.p1.name:
            self.p1.points += 1
        elif name == self.p2.name:
            self.p2.points += 1

    def score(self):
        if (self.p1.points < 4 and self.p2.points < 4) and (
            self.p1.points + self.p2.points < 6
        ):
            points = [LOVE, FIFTEEN, THIRTY, FORTY]
            player1_points = points[self.p1.points]
            return (
                player1_points + ALL
                if (self.p1.points == self.p2.points)
                else player1_points + "-" + points[self.p2.points]
            )
        else:
            if self.p1.points == self.p2.points:
                return DEUCE
            advantage_player = (
                self.p1.name
                if self.p1.points > self.p2.points
                else self.p2.name
            )
            return (
                WIN + advantage_player
                if abs(self.p1.points - self.p2.points) > 1
                else ADVANTAGE + advantage_player
            )
