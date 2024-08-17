from rest_framework import serializers

from .models import User
from apps.players.serializers import PlayerSerializer
from apps.planets.serializers import PlanetSerializer

class UserSerializer(serializers.ModelSerializer):
    urls = serializers.JSONField()
    planets = PlanetSerializer(many=True, read_only=True) 
    current_player = PlayerSerializer(read_only=True) 

    class Meta:
        model = User
        fields = (
            'id', 'current_player', 'planets', 'urls'
        )
