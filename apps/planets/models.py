from django.db import models
from django.urls import reverse
from apps.common.models import BaseModel
from django_lifecycle import hook

class Planet(BaseModel):
    player = models.ForeignKey('players.Player', on_delete=models.CASCADE, related_name='planets')
    name = models.CharField(max_length=100)
    home_planet = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    @hook('after_save')
    def create_iron_for_planet(instance, **kwargs):
        if instance.pk is not None and not hasattr(instance, 'iron'):
            from apps.resources.models import Iron
            Iron.objects.create(planet=instance)
    
    @hook('after_save')
    def create_mine_for_iron(instance, **kwargs):
        if instance.pk is not None and not hasattr(instance, 'mine'):
            from apps.resources.models import IronMine
            IronMine.objects.create(planet=instance)

    @property
    def urls(self):
        return {
            "select": reverse("api:planets-select-planet", kwargs={ "pk": self.id })
        }
    
