from django.urls import path

from bundesliga.liga.views import get_teams, next_match, season_matches

urlpatterns = (
    path('', get_teams, name='get_teams'),
    path('next_match', next_match, name='next_match'),
    path('season_matches', season_matches, name='season_matches'),
)
