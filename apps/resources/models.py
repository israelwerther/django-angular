from django.db import models
from apps.common.models import BaseModel
from django_lifecycle import hook
import datetime
from django.urls import reverse

class IronMine(BaseModel):
    planet = models.OneToOneField('planets.Planet', on_delete=models.CASCADE, related_name='iron_mine')
    level = models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
    def resources_required_for_upgrade(self):
        base_iron = 100
        growth_factor = 1.5
        return int(base_iron * (self.level + 1) ** growth_factor)
    
    def upgrade_duration(self):
        base_time = 20
        growth_factor = 1.2
        duration_in_minutes = base_time * (self.level ** growth_factor)
        return datetime.timedelta(minutes=duration_in_minutes)
    
    @property
    def urls(self):
        return {
            "select": reverse("api:resources-iron-mine-update-mine", kwargs={ "pk": self.id })
        }

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

