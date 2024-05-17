from django.urls import path
from .views import PlayerCreateAPIView, PlayerListAPIView, PlayerUpdateAPIView, PlayerDeleteAPIView

urlpatterns = [
     path('players/create/', PlayerCreateAPIView.as_view(), name='player-create'),
     path('players/list/', PlayerListAPIView.as_view(), name='player-list'),
     path('players/update/<int:pk>/', PlayerUpdateAPIView.as_view(), name='player-update'),
     path('players/delete/<int:pk>/', PlayerDeleteAPIView.as_view(), name='player-delete'),
]