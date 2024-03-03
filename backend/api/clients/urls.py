from django.urls import path
from .views import ClientCreateAPIView

urlpatterns = [
     path('clients/create/', ClientCreateAPIView.as_view(), name='client-create'),
]