# -*- coding: utf-8 -*-
from tennis_game import TennisGame
from tie_break import TieBreak


def score_player(player):
    return player.name + ": " + str(player.game_won)


class TennisSet:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_game = TennisGame(self.player1, self.player2)
        self.winner = None

    def won_point(self, player_name):
        if self.winner is not None:
            raise Exception("Set is over, " + self.winner.name + " has won")
        if self.current_game.winner is None:
            self.current_game.won_point(player_name)
        if self.current_game.winner is not None:
            # check if a player has won the set
            if max(self.player1.game_won, self.player2.game_won) >= 6:
                if abs(self.player1.game_won - self.player2.game_won) >= 2:
                    self.winner = (
                        self.player1
                        if self.player1.game_won > self.player2.game_won
                        else self.player2
                    )
                elif max(self.player1.game_won, self.player2.game_won) > 6:
                    self.winner = (
                        self.player1 if self.player1.game_won > 6 else self.player2
                    )

            if self.player1.game_won == 6 and self.player2.game_won == 6:
                self.current_game = TieBreak(self.player1, self.player2)
            elif self.winner is None:
                self.current_game = TennisGame(self.player1, self.player2)

    def score(self):
        return (
            score_player(self.player1)
            + "\n"
            + score_player(self.player2)
            + "\n"
            + (
                "Win for " + str(self.winner.name)
                if self.winner is not None
                else self.current_game.score()
            )
        )
