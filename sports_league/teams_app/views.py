from rest_framework import generics
from .models import Conference, Team, Player
from .serializers import ConferenceSerializer, TeamSerializer, PlayerSerializer

class ConferenceList(generics.ListAPIView):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer

class TeamList(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class PlayerList(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

# Implement detail views for each model as needed, following the ListAPIView pattern.
