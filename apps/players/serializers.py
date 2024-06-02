from django.forms import JSONField
from rest_framework import serializers
from .models import Player, Iron
from apps.resources.serializers import IronSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer

class PlayerSerializer(WritableNestedModelSerializer):
    # iron = IronSerializer(required=False)

    urls = JSONField()
    class Meta:
        model = Player
        fields = (
            'id', 'name', 'username', 'email',  'created_at', 'updated_at', 'get_current_iron', 'user', 'urls'
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