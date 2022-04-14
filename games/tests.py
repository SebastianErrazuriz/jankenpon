from django.test import TestCase

from .models import Game
from django.contrib.auth.models import User


class GameModelTests(TestCase):

    def test_system_hand_paper_win_player_rock(self):
        player = User.objects.create()
        game = Game(player=player, hand=Game.ROCK, system_hand=Game.PAPER)
        self.assertIs(game.does_system_hand_win(), True)

    def test_system_hand_rock_win_player_scissors(self):
        player = User.objects.create()
        game = Game(player=player, hand=Game.SCISSORS, system_hand=Game.ROCK)
        self.assertIs(game.does_system_hand_win(), True)