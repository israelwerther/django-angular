from django.shortcuts import render

from .models import Iron
from .serializers import IronSerializer
from rest_framework import viewsets

class IronModelViewSet(viewsets.ModelViewSet):
    queryset = Iron.objects.all()
    serializer_class = IronSerializer
    model = Iron