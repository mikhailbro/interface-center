import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Application(models.Model):
    app_id = models.CharField(max_length=10, default='', verbose_name='APP-ID')
    short_name = models.CharField(max_length=20, default='')
    mail_address = models.EmailField(max_length=60, default='')


    def __str__(self):
        return self.app_id + " (" + self.short_name + ")"
