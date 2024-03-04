from django.urls import path
from .views import ClientCreateAPIView, ClientListAPIView

urlpatterns = [
     path('clients/create/', ClientCreateAPIView.as_view(), name='client-create'),
     path('clients/list/', ClientListAPIView.as_view(), name='client-list'),
]