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

    # def get_queryset(self):
    #     return Player.objects.filter(user=self.request.user)

    @action(detail=True, methods=['get'])
    def select_player(self, request, pk=None):
        player = self.get_object()        
        user = request.user
        user.current_player = player
        user.save()
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
