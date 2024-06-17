from django.db import models
import uuid

class BaseModole(models.Model):
    udid = models.UUIDField(primary_key=True , editable=False , default=uuid.uuid4)
    create_at = models.DateField(auto_now=True)
    upate_date_by = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

