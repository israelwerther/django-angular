from django.db import models

class Client(models.Model):
    name = models.CharField("Nome do Cliente", max_length=255)

    def __str__(self):
        return self.name