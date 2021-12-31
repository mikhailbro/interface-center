import datetime
from django.db import models
from django.contrib.auth.models import User
from app_interface.models import Interface
from app_application.models import Application



# Create your models here.
class Review(models.Model):
    interface = models.ForeignKey(Interface, on_delete=models.CASCADE, default=None)
    


    def __str__(self):
        return self.name + "- " + str(self.status)