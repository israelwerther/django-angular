from rest_framework import serializers
from apps.planets.models import Planet
from apps.resources.serializers import IronSerializer

class PlanetSerializer(serializers.ModelSerializer):
    iron = IronSerializer(read_only=True)

    class Meta:
        model = Planet
        fields = ('id', 'name', 'home_planet', 'iron')
