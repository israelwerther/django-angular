from django.db import models
from apps.common.models import BaseModel
from django_lifecycle import hook
import datetime

class IronMine(BaseModel):
    iron = models.OneToOneField('Iron', on_delete=models.CASCADE, related_name='mine')
    level = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)

class Iron(BaseModel):
    planet = models.OneToOneField('planets.Planet', on_delete=models.CASCADE, related_name='iron')
    quantity = models.IntegerField(default=0)

    @hook('after_save')
    def create_mine_for_iron(instance, **kwargs):
        if instance.pk is not None and not hasattr(instance, 'mine'):
            IronMine.objects.create(iron=instance)

    def __str__(self):
        return str(self.id)

    def get_current_iron(self):
        if not self:
            return 0

        time_diff = datetime.datetime.now(tz=self.updated_at.tzinfo) - self.updated_at
        iron_per_second = 1
        generated_iron = int(time_diff.total_seconds() * iron_per_second)

        return self.quantity + generated_iron

