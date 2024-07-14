# Create your models here.
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    current_player = models.ForeignKey('players.Player', null=True, blank=True, on_delete=models.SET_NULL)