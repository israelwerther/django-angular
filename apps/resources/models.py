from django.db import models

class Iron(models.Model):
    quantity = models.IntegerField(default=0)
    player = models.OneToOneField('players.Player', on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    
    def __str__(self):
        return str(self.id)
