from django.shortcuts import render

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