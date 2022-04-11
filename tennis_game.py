# -*- coding: utf-8 -*-
from player import Player


class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def won_point(self, player_name):
        if player_name == self.player1.name:
            self.player1.score += 1
        else:
            self.player2.score += 1

    def score(self):
        if (self.player1.score < 4 and self.player2.score < 4) and (
            self.player1.score + self.player2.score < 6
        ):
            # no player have scored more than 4 points and less than 6 points have been played
            score_value = ["Love", "Fifteen", "Thirty", "Forty"]
            advantage_player = score_value[self.player1.score] + "-"
            return advantage_player + (
                "All"
                if (self.player1.score == self.player2.score)
                else score_value[self.player2.score]
            )
        else:
            if self.player1.score == self.player2.score:
                return "Deuce"
            advantage_player = (
                self.player1.name
                if self.player1.score > self.player2.score
                else self.player2.name
            )
            score = (
                "Win for "
                if abs(self.player1.score - self.player2.score) > 1
                else "Advantage "
            )
            return score + advantage_player
