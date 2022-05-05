import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Application(models.Model):
    app_id = models.CharField(max_length=10, default='', verbose_name='APP-ID')
    short_name = models.CharField(max_length=20, null=True, blank=True, default=None)
    mail_address = models.EmailField(max_length=60, null=True, blank=True, default=None)

    status_choices=[('PLANNED', 'Planned'), ('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')]
    status = models.CharField( max_length=20, choices=status_choices, default='PLANNED')


    def __str__(self):
        return f"{self.app_id}"
