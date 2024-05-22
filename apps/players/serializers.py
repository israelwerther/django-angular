from rest_framework import serializers
from .models import Player
from apps.resources.serializers import IronSerializer

class PlayerSerializer(serializers.ModelSerializer):
    iron = IronSerializer()

    class Meta:
        model = Player
        fields = ('id', 'name', 'username', 'email', 'iron')