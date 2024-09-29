from rest_framework import serializers
from .models import Player
from apps.planets.serializers import PlanetSerializer

class PlayerSerializer(serializers.ModelSerializer):
    urls = serializers.JSONField(read_only=True)
    planets = PlanetSerializer(many=True, read_only=True) 

    class Meta:
        model = Player
        fields = (
            'id', 'name', 'username', 'email', 'created_at', 'updated_at', 'user', 'urls', 'planets', 'current_planet'
        )
