from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    last_update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
