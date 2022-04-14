from django import forms

from games.models import Game


class GameForm(forms.Form):
    hand = forms.ChoiceField(choices=Game.HAND_CHOICES)


class GameModelForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['hand']

