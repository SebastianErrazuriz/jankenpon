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
    created_at = models.DateTimeField(auto_now_add=True)