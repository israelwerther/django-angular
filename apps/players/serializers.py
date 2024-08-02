from rest_framework import serializers
from .models import Player
from apps.planets.serializers import PlanetSerializer

class PlayerSerializer(serializers.ModelSerializer):
    urls = serializers.JSONField()
    planets = PlanetSerializer(many=True, read_only=True) 

    class Meta:
        model = Player
        fields = (
            'id', 'name', 'username', 'email', 'created_at', 'updated_at', 'user', 'urls', 'planets'
        )

    

    # def create(self, validated_data):
    #     iron_data = validated_data.pop('iron', None)
    #     player = Player.objects.create(**validated_data)

    #     if iron_data is not None:
    #         iron = Iron.objects.create(**iron_data)
    #         player.iron = iron
    #         player.save()

    #     return player

    # def to_representation(self, instance):
    #     representation = super(PlayerSerializer, self).to_representation(instance)

    #     if instance.iron is not None:
    #         representation['iron'] = IronSerializer(instance.iron).data
    #     else:
    #         representation['iron'] = None

    #     return representation