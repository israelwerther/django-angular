from django.shortcuts import render

from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from .models import Player
from .serializers import PlayerSerializer


class PlayerCreateAPIView(CreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerListAPIView(ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerUpdateAPIView(UpdateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerDeleteAPIView(DestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer