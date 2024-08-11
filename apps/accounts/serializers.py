from rest_framework import serializers
from .models import User
from apps.planets.serializers import PlanetSerializer

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'current_player'
        )
