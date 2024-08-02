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

    def __str__(self):
        return self.name
    
    @hook('after_save')
    def create_home_planet(instance, **kwargs):
        if instance.pk is not None and not instance.planets.exists():
            from apps.planets.models import Planet
            Planet.objects.create(player=instance, name="Home Planet", home_planet=True)

    # def get_current_iron(self):
    #     if not self.iron:
    #         return 0

    #     time_diff = datetime.now(tz=self.iron.updated_at.tzinfo) - self.iron.updated_at
    #     iron_per_second = 1
    #     generated_iron = int(time_diff.total_seconds() * iron_per_second)

    #     return self.iron.quantity + generated_iron
    
    # @hook('after_save')
    # def create_iron_for_player(instance, **kwargs):
    #     if instance.pk is not None and instance.iron is None:
    #         iron_obj = Iron.objects.create(player=instance)
    #         instance.iron = iron_obj
    #         instance.save()
    

    @property
    def urls(self): 
        return {
            "select": reverse("api:players-select-player", kwargs={ "pk": self.id })
        }
            
    