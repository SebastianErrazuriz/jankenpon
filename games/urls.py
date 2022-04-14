from django.urls import path

from . import views
app_name = 'games'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:game_id>', views.detail, name='detail'),
    path('new_game', views.new_game, name='new_game'),
]

