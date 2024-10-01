from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.planets.models import Planet
from apps.planets.serializers import PlanetSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

@method_decorator(csrf_exempt, name='dispatch')
class PlanetModelViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def select_planet(self, request, pk=None):
        planet = self.get_object()
        user = request.user
        player = user.current_player
        player.current_planet = planet
        player.save()
        serializer = self.get_serializer(planet)
        return Response(serializer.data)
