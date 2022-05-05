from django.shortcuts import render
from datetime import datetime, date, time

from django.views.generic import ListView

from bundesliga.liga.OpenLigaDbApi import API

'''Sport: Soccer'''
sportID = "1"

'''Shortcut of league'''
leagueShortcut = "bl1"

'''ID of 3. Fußball-Bundesliga 2021/2022'''
leagueId = "4500"

'''Season of league'''
leagueSaison = "2021"

'''No. of matchday'''
groupOrderID = "1"
'''ID of Bayern Muenchen'''
teamID1 = "40"
'''ID of Borussia Moenchengladbach'''
teamID2 = "87"
'''Bayern Muenchen - Borussia Moenchengladbach'''
matchID = "23711"
'''Startdate of 1.BL 2013'''
fromDateTime = datetime.combine(datetime(2013, 8, 9), time(0, 0, 0))
'''Enddate'''
toDateTime = datetime.combine(date.today(), time(0, 0, 0))

api = API()

currentGroup = api.getCurrentGroup(leagueShortcut)
print("Current Group: ", currentGroup)


# Create your views here.

def get_teams(request):
    teams = api.getTeamsByLeagueSaison(leagueShortcut, leagueSaison)
    context = {
        'teams': teams[0],
    }
    return render(request, 'teams.html', context)


def next_match(request):
    next_match_info = api.getNextMatch(leagueShortcut)
    context = {"match": next_match_info}
    return render(request, 'next_match.html', context)


def season_matches(request):
    matches_info = api.getMatchdataByLeagueSaison(leagueShortcut, leagueSaison)
    context = {"matches": matches_info[0]}
    return render(request, 'season_matches.html', context)



