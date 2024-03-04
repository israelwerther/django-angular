from django.urls import path
from .views import ClientCreateAPIView, ClientListAPIView, ClientUpdateAPIView, ClientDeleteAPIView

urlpatterns = [
     path('clients/create/', ClientCreateAPIView.as_view(), name='client-create'),
     path('clients/list/', ClientListAPIView.as_view(), name='client-list'),
     path('clients/update/<int:pk>/', ClientUpdateAPIView.as_view(), name='client-update'),
     path('clients/delete/<int:pk>/', ClientDeleteAPIView.as_view(), name='client-delete'),
]