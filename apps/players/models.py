from django.db import models
from apps.resources.models import Iron
from apps.common.models import BaseModel

class Player(BaseModel):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    iron = models.OneToOneField(Iron, on_delete=models.CASCADE, related_name='player_iron', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            iron_obj = Iron.objects.create()
            self.iron = iron_obj
        super(Player, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
