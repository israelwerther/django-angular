from django.shortcuts import render

from apps.resources.models import Iron
from apps.resources.serializers import IronSerializer

from .models import Player
from .serializers import PlayerSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
import random

class PlayerModelViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    model = Player

    @action(detail=False, methods=['post'])
    def create_player_with_iron(self, request):
        random_number = random.randint(1, 100)  # generate a random number
        iron_obj = Iron.objects.create(number=random_number)  # create a new Iron object with the random number

        request.data['iron'] = iron_obj.pk  # associate the Iron object with the Player
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

# class IronModelViewSet(viewsets.ModelViewSet):
#     queryset = Iron.objects.all()
#     serializer_class = IronSerializer





    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset


    # @action(detail=False, methods=["GET"])
    # def list_users(self,request, pk=None):
        
    #     return Response(
    #         data=PlayerSerializer(
    #             instance=self.get_queryset(), 
    #             many=True
    #         ).data
    #     )