import datetime
from django.db import models
from apps.common.models import BaseModel
from django_lifecycle import hook


class Iron(BaseModel):
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.id)
    
    def get_current_iron(self):
        if not self:
            return 0

        time_diff = datetime.datetime.now(tz=self.updated_at.tzinfo) - self.updated_at
        iron_per_second = 1
        generated_iron = int(time_diff.total_seconds() * iron_per_second)

        return self.quantity + generated_iron

class IronMine(BaseModel):
    planet = models.ForeignKey('planets.Planet', on_delete=models.SET_NULL, null=True, blank=True)
    iron = models.OneToOneField(Iron, on_delete=models.CASCADE, related_name='iron_mine', null=True, blank=True)


    @hook('after_save')
    def create_iron_for_mine(instance, **kwargs):
        if instance.pk is not None and instance.iron is None:
            iron_obj = Iron.objects.create()
            instance.iron = iron_obj
            instance.save()


    def __str__(self):
        return str(self.id)

