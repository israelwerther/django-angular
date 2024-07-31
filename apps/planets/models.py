from django.db import models
from apps.common.models import BaseModel
from apps.players.models import Player

class Planet(BaseModel):
    player = models.ForeignKey('players.Player', on_delete=models.CASCADE, related_name='planets')
    name = models.CharField(max_length=100)
    home_planet = models.BooleanField(default=False)

    def __str__(self):
        return self.name