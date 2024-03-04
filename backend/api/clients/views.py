from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from .models import Client
from .serializers import ClientSerializer


class ClientCreateAPIView(CreateAPIView):
    print("========")
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientListAPIView(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientUpdateAPIView(UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDeleteAPIView(DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer