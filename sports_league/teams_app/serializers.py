from rest_framework import serializers
from .models import Conference, Team, Player

class ConferenceSerializer(serializers.HyperlinkedModelSerializer):
    teams = serializers.HyperlinkedRelatedField(many=True, view_name='team-detail', read_only=True)

    class Meta:
        model = Conference
        fields = ['id', 'name', 'teams']

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    players = serializers.HyperlinkedRelatedField(many=True, view_name='player-detail', read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'location', 'conference', 'wins', 'losses', 'players']

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'name', 'position', 'age', 'is_injured_reserve', 'points', 'team']
