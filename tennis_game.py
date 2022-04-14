# -*- coding: utf-8 -*-


class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player1.game_score = 0
        self.player2.game_score = 0
        self.winner = None
        self.score_value = "Love-All"

    def won_point(self, player_name):
        if self.winner is not None:
            raise Exception("Game is over")
        if player_name == self.player1.name:
            self.player1.game_score += 1
        elif player_name == self.player2.name:
            self.player2.game_score += 1
        else:
            raise Exception(player_name + " is not playing")
        self.score_value = self.get_score()

    def get_score(self):
        if self.winner is not None:
            return self.score_value
        if (self.player1.game_score < 4 and self.player2.game_score < 4) and (
            self.player1.game_score + self.player2.game_score < 6
        ):
            # no player have scored more than 4 points and less than 6 points have been played
            score_value = ["Love", "Fifteen", "Thirty", "Forty"]
            advantage_player = score_value[self.player1.game_score] + "-"
            return advantage_player + (
                "All"
                if (self.player1.game_score == self.player2.game_score)
                else score_value[self.player2.game_score]
            )
        else:
            if self.player1.game_score == self.player2.game_score:
                return "Deuce"
            advantage_player = (
                self.player1.name
                if self.player1.game_score > self.player2.game_score
                else self.player2.name
            )
            if abs(self.player1.game_score - self.player2.game_score) > 1:
                score = "Win for "
                self.winner = (
                    self.player1
                    if self.player1.game_score > self.player2.game_score
                    else self.player2
                )
                self.winner.game_won += 1
            else:
                score = "Advantage "
            return score + advantage_player

    def score(self):
        return self.score_value
