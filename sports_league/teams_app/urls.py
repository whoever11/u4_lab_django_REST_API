from django.urls import path
from .views import ConferenceList, TeamList, PlayerList

urlpatterns = [
    path('conferences/', ConferenceList.as_view(), name='conference-list'),
    path('teams/', TeamList.as_view(), name='team-list'),
    path('players/', PlayerList.as_view(), name='player-list'),
    # Add detail views URLs as needed
]
