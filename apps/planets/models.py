from django.db import models
from apps.common.models import BaseModel
from apps.players.models import Player

class Planet(BaseModel):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='planets')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name