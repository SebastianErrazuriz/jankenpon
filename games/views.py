import random

from django.shortcuts import get_object_or_404, render, redirect

from games.forms import GameForm, GameModelForm
from games.models import Game


def index(request):
    latest_game_list = Game.objects.order_by('-created_at')[:10]
    context = {'latest_game_list': latest_game_list}
    return render(request, 'games/index.html', context)


def detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'games/detail.html', {'game': game})


def new_game(request):
    if request.method == 'POST':
        new_game_form = GameModelForm(request.POST)
        if new_game_form.is_valid():
            new_game_instance = new_game_form.save(commit=False)
            new_game_instance.player = request.user
            # random choice of hand
            new_game_instance.system_hand = random.choice([Game.ROCK, Game.PAPER, Game.SCISSORS])
            new_game_instance.system_won = new_game_instance.does_system_hand_win()
            new_game_instance.save()

            return redirect('games:detail', game_id=new_game_instance.pk)

    else:
        new_game_form = GameForm()

    return render(request, 'games/new_game.html', {'form': new_game_form})
