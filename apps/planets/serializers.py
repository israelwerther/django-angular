from rest_framework import serializers
from apps.planets.models import Planet
from apps.resources.serializers import IronSerializer, IronMineSerializer

class PlanetSerializer(serializers.ModelSerializer):
    iron = IronSerializer(read_only=True)
    iron_mine = IronMineSerializer(read_only=True)

    class Meta:
        model = Planet
        fields = ('id', 'name', 'home_planet', 'iron', 'urls', 'iron_mine')
