import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.players.models import Player

class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    current_player = models.ForeignKey(Player, null=True, blank=True, on_delete=models.SET_NULL, related_name='current_user')