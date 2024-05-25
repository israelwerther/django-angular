from django.contrib.auth.models import User
from django.db import models
from apps.resources.models import Iron
from apps.common.models import BaseModel
from datetime import datetime, timedelta

class Player(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='players')
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    iron = models.OneToOneField(Iron, on_delete=models.CASCADE, related_name='player_iron', null=True, blank=True)
    
    # def save(self, *args, **kwargs):
    #     if self.pk is None:
    #         iron_obj = Iron.objects.create()
    #         self.iron = iron_obj
    #     super(Player, self).save(*args, **kwargs)

    # def __str__(self):
    #     return self.name
    
    def get_current_iron(self):
        if not self.iron:
            return 0

        time_diff = datetime.now(tz=self.iron.updated_at.tzinfo) - self.iron.updated_at
        iron_per_second = 1
        generated_iron = int(time_diff.total_seconds() * iron_per_second)

        return self.iron.quantity + generated_iron
