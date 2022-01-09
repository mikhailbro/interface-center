import datetime
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from app_interface.models import Interface


# Create your models here.
class Review(models.Model):
    interface = models.ForeignKey(Interface, on_delete=models.CASCADE, default=None)
    requestor = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None, related_name='requestor')
    reviewer = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None, related_name='reviewer')
    created_at = models.DateField(default=datetime.date.today)

    #findings = ArrayField(models.TextField(max_length=300, default=None), size=10, null=True, blank=True, default=None)
    #findings = models.JSONField(default=list, blank=True, null=True)
    #findings = models.TextField(max_length=500, null=True, blank=True, default=None)

    class ReviewStatusEnum(models.TextChoices):
        REQUESTED = 'REQUESTED', ('Requested')
        PROCESSING = 'PROCESSING', ('Processing')
        DONE = 'DONE', ('Done')
        
    review_status = models.CharField(
        max_length=15,
        choices=ReviewStatusEnum.choices,
        default=ReviewStatusEnum.REQUESTED,
    )

    def __str__(self):
        return f"{self.interface.interface_id}-Review-{self.created_at}"