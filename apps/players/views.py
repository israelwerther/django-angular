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
    


    # @action(detail=False, methods=["GET"])
    # def list_users(self,request, pk=None):
        
    #     return Response(
    #         data=PlayerSerializer(
    #             instance=self.get_queryset(), 
    #             many=True
    #         ).data
    #     )
