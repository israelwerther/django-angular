from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from apps.resources.models import Iron

class Player(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    iron = models.OneToOneField(Iron, on_delete=models.CASCADE, related_name='player_iron', null=True, blank=True)

    def save(self, *args, **kwargs):
        # Verifica se é um novo jogador
        if self.pk is None:
            # Cria um novo recurso Iron
            iron_obj = Iron.objects.create()
            # Vincula o recurso Iron ao jogador
            self.iron = iron_obj
        # Chama o método save() da superclasse
        super(Player, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
