from .models import Player
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import PlayerSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action



@method_decorator(csrf_exempt, name='dispatch')
class PlayerModelViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Player.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['get'])
    def select_player(self, request, pk=None):
        player = self.get_object()        
        user = request.user
        user.current_player = player
        
        home_planet = player.planets.filter(home_planet=True).first()
        
        if home_planet:
            player.current_planet = home_planet
            player.save()
        
        user.save()
        serializer = self.get_serializer(player)
        return Response(serializer.data)
