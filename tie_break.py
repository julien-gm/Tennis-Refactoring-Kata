# -*- coding: utf-8 -*-
from tennis_game import TennisGame


class TieBreak(TennisGame):
    def __init__(self, player1, player2):
        TennisGame.__init__(self, player1, player2)
        self.score_value = "0-0"

    def won_point(self, player_name):
        TennisGame.won_point(self, player_name)

    def get_score(self):
        self.score_value = (
            str(self.player1.game_score) + "-" + str(self.player2.game_score)
        )
        if max(self.player1.game_score, self.player2.game_score) >= 7 and (
            abs(self.player1.game_score - self.player2.game_score) >= 2
        ):
            self.winner = (
                self.player1
                if self.player1.game_score > self.player2.game_score
                else self.player2
            )
            self.winner.game_won += 1

    def score(self):
        return str(self.player1.game_score) + "-" + str(self.player2.game_score)
