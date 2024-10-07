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
        iron = iron_mine.planet.iron
        current_iron = iron.get_current_iron()
        required_iron = iron_mine.resources_required_for_upgrade()

        if current_iron >= required_iron:
            iron_mine.level += 1
            iron_mine.save()
            

        serializer = self.get_serializer(iron_mine)
        response_data = serializer.data
        response_data['current_iron'] = current_iron
        response_data['resources_required_for_upgrade'] = required_iron

        return Response(response_data)