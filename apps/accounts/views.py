from django.shortcuts import render
from django.utils.decorators import method_decorator
from rest_framework import viewsets, status
from django.views.decorators.csrf import csrf_exempt

from apps.accounts.models import User
from apps.players.serializers import PlayerSerializer
from .serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


@method_decorator(csrf_exempt, name='dispatch')
class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def load_current_player(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        
        # Serializa o usuário e retorna os dados
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    
