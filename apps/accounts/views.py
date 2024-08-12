from django.shortcuts import render
from django.utils.decorators import method_decorator
from rest_framework import viewsets, status
from django.views.decorators.csrf import csrf_exempt

from apps.accounts.models import User
from .serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


@method_decorator(csrf_exempt, name='dispatch')
class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def select_planet(self, request, pk=None):
        planet = self.get_object()        
        user = request.user
        user.current_planet = planet
        user.save()
        serializer = self.get_serializer(planet)
        return Response(serializer.data)
