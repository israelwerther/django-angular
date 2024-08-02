from django.db import models
from apps.common.models import BaseModel
from apps.players.models import Player
from apps.resources.models import Iron
from django_lifecycle import hook

class Planet(BaseModel):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='planets')
    name = models.CharField(max_length=100)
    home_planet = models.BooleanField(default=False)
    # Iron usando iron.planet_iron. Isso é útil e geralmente uma boa prática
    iron = models.OneToOneField(Iron, on_delete=models.CASCADE, related_name='planet_iron', null=True, blank=True)

    @hook('after_save')
    def create_iron_for_planet(instance, **kwargs):
        if instance.pk is not None and instance.iron is None:
            iron_obj = Iron.objects.create()
            instance.iron = iron_obj
            instance.save()


    def __str__(self):
        return self.name
    
