from .models import Player
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import PlayerSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response

@method_decorator(csrf_exempt, name='dispatch')
class PlayerModelViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
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
