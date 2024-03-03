from rest_framework.generics import CreateAPIView
from .models import Client
from .serializers import ClientSerializer


class ClientCreateAPIView(CreateAPIView):
    print("========")
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
