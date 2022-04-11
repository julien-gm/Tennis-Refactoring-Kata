# -*- coding: utf-8 -*-
class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1Name = player1_name
        self.player2Name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1Name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def score(self):
        if (self.player1_score < 4 and self.player2_score < 4) and (
            self.player1_score + self.player2_score < 6
        ):
            # no player have scored more than 4 points and less than 6 points have been played
            score_value = ["Love", "Fifteen", "Thirty", "Forty"]
            advantage_player = score_value[self.player1_score] + "-"
            return advantage_player + (
                "All"
                if (self.player1_score == self.player2_score)
                else score_value[self.player2_score]
            )
        else:
            if self.player1_score == self.player2_score:
                return "Deuce"
            advantage_player = (
                self.player1Name
                if self.player1_score > self.player2_score
                else self.player2Name
            )
            score = (
                "Win for "
                if abs(self.player1_score - self.player2_score) > 1
                else "Advantage "
            )
            return score + advantage_player
