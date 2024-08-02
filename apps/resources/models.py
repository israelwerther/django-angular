import datetime
from django.db import models
from apps.common.models import BaseModel

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
