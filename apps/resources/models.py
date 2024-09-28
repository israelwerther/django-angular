import datetime
from django.db import models
from apps.common.models import BaseModel
from django_lifecycle import hook

class IronMine(BaseModel):
    level = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)

class Iron(BaseModel):
    quantity = models.IntegerField(default=0)
    mine = models.OneToOneField(IronMine, on_delete=models.CASCADE, null=True, blank=True)

    @hook('after_save')
    def create_mine(instance, **kwargs):
        if instance.pk is not None and instance.mine is None:
            mine_obj = IronMine.objects.create()
            instance.mine = mine_obj
            instance.save()
    
    def __str__(self):
        return str(self.id)
    
    def get_current_iron(self):
        if not self:
            return 0

        time_diff = datetime.datetime.now(tz=self.updated_at.tzinfo) - self.updated_at
        iron_per_second = 1
        generated_iron = int(time_diff.total_seconds() * iron_per_second)

        return self.quantity + generated_iron
