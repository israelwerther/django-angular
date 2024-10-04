from django.db import models
from apps.common.models import BaseModel
from django_lifecycle import hook
import datetime

class IronMine(BaseModel):
    planet = models.OneToOneField('planets.Planet', on_delete=models.CASCADE, related_name='iron_mine')
    level = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)
    
    def resources_required_for_upgrade(self):
        base_iron = 100
        growth_factor = 1.5
        return int(base_iron * (self.level + 1) ** growth_factor)

class Iron(BaseModel):
    planet = models.OneToOneField('planets.Planet', on_delete=models.CASCADE, related_name='iron')
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

