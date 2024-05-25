from django_lifecycle import LifecycleModelMixin

from django.db import models

import uuid

class BaseModel(LifecycleModelMixin, models.Model):
	# id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
	created_at = models.DateTimeField(verbose_name='Created at', auto_now=True)
	updated_at = models.DateTimeField(verbose_name='Updated at', auto_now=True)

	class Meta:
		abstract = True