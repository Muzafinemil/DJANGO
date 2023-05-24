from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='home'),
    path('match/', MatchPage.as_view(), name='match'),
    path('player/', PlayersPage.as_view(), name='player'),
    path('tournament/', TournamentPage.as_view(), name='tournament'),
    path('team/', TeamPage.as_view(), name='team'),
    path('teamadd/', TeamADD.as_view(), name='addteam'),
    path('teamdelete/<int:pk>/', TeamDelete.as_view(), name='deleteteam'),
    path('teamupdate/<int:pk>/', TeamUpdate.as_view(), name='updateteam'),
]
