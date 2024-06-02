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

    @action(detail=True, methods=['get'])
    def select_player(self, request, pk=None):
        player_id = 1  # Aqui você pode passar o ID do jogador que deseja selecionar
        player = self.get_object()  # Use get_object_or_404 para obter o jogador
        serializer = self.get_serializer(player)
        return Response(serializer.data)


    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


    # model = Player
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]



    # @action(detail=False, methods=["GET"])
    # def list_users(self,request, pk=None):
        
    #     return Response(
    #         data=PlayerSerializer(
    #             instance=self.get_queryset(), 
    #             many=True
    #         ).data
    #     )
