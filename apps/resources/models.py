from django.db import models
from apps.common.models import BaseModel

class Iron(BaseModel):
    player = models.OneToOneField('players.Player', on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.id)
