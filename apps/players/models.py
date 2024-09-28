from django.db import models
from django.urls import reverse
from core import settings
from django_lifecycle import hook
from apps.common.models import BaseModel

class Player(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='players', null=True, blank=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    current_planet = models.ForeignKey('planets.Planet', null=True, blank=True, on_delete=models.SET_NULL, related_name='current_planet')

    def __str__(self):
        return self.name
    
    @hook('after_save')
    def create_home_planet(instance, **kwargs):
        if instance.pk is not None and not instance.planets.exists():
            from apps.planets.models import Planet
            Planet.objects.create(player=instance, name="Home Planet", home_planet=True)

    @property
    def urls(self):
        return {
            "select": reverse("api:players-select-player", kwargs={ "pk": self.id })
        }
            
    