import datetime
from django.db import models
from django.contrib.auth.models import User
from app_interface.models import Interface
from app_application.models import Application



# Create your models here.
class Implementation(models.Model):
    interface = models.ForeignKey(Interface, on_delete=models.CASCADE, default=None)
    provider = models.ForeignKey(Application, on_delete=models.DO_NOTHING, default=None)
    provider_basepath = models.CharField(max_length=100, default='')
    implementation_counter = models.PositiveIntegerField(default=1)

    class ImplementationTypeEnum(models.TextChoices):
        WEB_SERVICE = 'WEB_SERVICE', ('Web Service')
        API = 'API', ('Api')
        QUEUE = 'QUEUE', ('Queue')
        
    implementation_type = models.CharField(
        max_length=20,
        choices=ImplementationTypeEnum.choices,
        default=ImplementationTypeEnum.API,
    )   


    def __str__(self):
        return self.name + "- " + str(self.status)