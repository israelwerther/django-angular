from rest_framework import serializers
from .models import User
from apps.planets.serializers import PlanetSerializer

class UserSerializer(serializers.ModelSerializer):
    urls = serializers.JSONField()
    planets = PlanetSerializer(many=True, read_only=True) 

    class Meta:
        model = User
        fields = (
            'id', 'current_player', 'current_planet',  'planets', 'urls'
        )
