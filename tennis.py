# -*- coding: utf-8 -*-


class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0


class TennisGame:
    def __init__(self, player1Name, player2Name):
        self.player1 = Player(player1Name)
        self.player2 = Player(player2Name)
        self.winner = None
        self.result = self.calculate_score()

    def won_point(self, playerName):
        if playerName not in (self.player1.name, self.player2.name):
            raise Exception(playerName + " is not playing")
        if self.winner is not None:
            raise Exception("Game is over")
        if playerName == self.player1.name:
            self.player1.points += 1
        else:
            self.player2.points += 1
        self.result = self.calculate_score()

    def score(self):
        return self.result

    def calculate_score(self):
        if (self.player1.points < 4 and self.player2.points < 4) and (
            self.player1.points + self.player2.points < 6
        ):
            points = ["Love", "Fifteen", "Thirty", "Forty"]
            player = points[self.player1.points]
            return (
                player + "-All"
                if (self.player1.points == self.player2.points)
                else player + "-" + points[self.player2.points]
            )
        else:
            if self.player1.points == self.player2.points:
                return "Deuce"
            player = (
                self.player1
                if self.player1.points > self.player2.points
                else self.player2
            )
            if abs(self.player1.points - self.player2.points) == 1:
                return "Advantage " + player.name
            else:
                self.winner = player
                return "Win for " + player.name
