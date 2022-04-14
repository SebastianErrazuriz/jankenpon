from django.db import models
from django.conf import settings


class Game(models.Model):
    ROCK = 'ROCK'
    PAPER = 'PAPER'
    SCISSORS = 'SCISSORS'

    HAND_CHOICES = [
        (ROCK, 'rock'),
        (PAPER, 'paper'),
        (SCISSORS, 'scissors'),
    ]
    player = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    hand = models.CharField(
        max_length=8,
        choices=HAND_CHOICES,
    )
    system_hand = models.CharField(
        max_length=8,
        choices=HAND_CHOICES,
        default=PAPER
    )
    system_won = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player} {self.hand} ({'Player LOST' if self.system_won else 'Player WIN'})"

    def does_system_hand_win(self):
        if self.hand == self.ROCK and self.system_hand == self.PAPER:
            return True
        elif self.hand == self.PAPER and self.system_hand == self.SCISSORS:
            return True
        elif self.hand == self.SCISSORS and self.system_hand == self.ROCK:
            return True
        return False
