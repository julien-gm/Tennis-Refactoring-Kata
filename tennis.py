# -*- coding: utf-8 -*-


class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0


class TennisGame:
    def __init__(self, player1Name, player2Name):
        self.player1 = Player(player1Name)
        self.player2 = Player(player2Name)
        self.win = 0

    def won_point(self, playerName):
        if self.win == 1:
            raise Exception("Game is over")
        elif playerName == self.player1.name:
            self.player1.points += 1
        elif playerName == self.player2.name:
            self.player2.points += 1
        elif playerName != self.player1.name or playerName != self.player2.name:
            raise Exception(playerName + " is not playing")

    def score(self):
        if (self.player1.points < 4 and self.player2.points < 4) and (
            self.player1.points + self.player2.points < 6
        ):
            points = ["Love", "Fifteen", "Thirty", "Forty"]
            score = points[self.player1.points]
            return (
                score + "-All"
                if (self.player1.points == self.player2.points)
                else score + "-" + points[self.player2.points]
            )
        else:
            score = (
                self.player1.name
                if self.player1.points > self.player2.points
                else self.player2.name
            )
            if self.player1.points == self.player2.points:
                return "Deuce"
            elif (
                (self.player1.points - self.player2.points)
                * (self.player1.points - self.player2.points)
            ) == 1:
                return "Advantage " + score
            else:
                self.win = 1
                return "Win for " + score
