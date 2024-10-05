from rest_framework.decorators import action
from .models import Iron, IronMine
from .serializers import IronMineSerializer, IronSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class IronModelViewSet(viewsets.ModelViewSet):
    queryset = Iron.objects.all()
    serializer_class = IronSerializer
    model = Iron

class IronMineModelViewSet(viewsets.ModelViewSet):
    queryset = IronMine.objects.all()
    serializer_class = IronMineSerializer
    model = IronMine

    @action(detail=True, methods=['get'])
    def update_mine(self, request, pk=None):
        iron_mine = self.get_object()
        print('iron_mine::: ', iron_mine)
        
        serializer = self.get_serializer(iron_mine)
        return Response(serializer.data)