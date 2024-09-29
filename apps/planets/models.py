from django.db import models
from django.urls import reverse
from apps.common.models import BaseModel
from django_lifecycle import hook

class Planet(BaseModel):
    player = models.ForeignKey('players.Player', on_delete=models.CASCADE, related_name='planets')
    name = models.CharField(max_length=100)
    home_planet = models.BooleanField(default=False)

    @hook('after_save')
    def create_iron_for_planet(instance, **kwargs):
        if instance.pk is not None and not hasattr(instance, 'iron'):
            from apps.resources.models import Iron
            Iron.objects.create(planet=instance)

    def __str__(self):
        return self.name
    
    @property
    def urls(self):
        return {
            "select": reverse("api:planets-select-planet", kwargs={ "pk": self.id })
        }
    
