# -*- coding: utf-8 -*-

import pytest

from tennis_unittest import game_test_cases, play_game
from player import Player


class TestTennis:
    @pytest.mark.parametrize(
        "p1_points p2_points score p1_name p2_name".split(), game_test_cases
    )
    def test_get_score_game(self, p1_points, p2_points, score, p1_name, p2_name):
        player1 = Player(p1_name)
        player2 = Player(p2_name)
        game = play_game(p1_points, p2_points, player1, player2)
        assert score == game.score()
