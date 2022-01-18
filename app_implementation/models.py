from django.db import models
from app_interface.models import Interface
from app_application.models import Application



# Create your models here.
class Implementation(models.Model):
    interface = models.ForeignKey(Interface, on_delete=models.CASCADE, default=None)
    provider = models.ForeignKey(Application, on_delete=models.DO_NOTHING, default=None, related_name='provider')
    provider_basepath = models.CharField(max_length=100, default='')
    implementation_counter = models.PositiveIntegerField(default=1)
    consumers = models.ManyToManyField(Application, blank=True, related_name='consumers')

    class ImplementationTypeEnum(models.TextChoices):
        API = 'API', ('API')
        WEB_SERVICE = 'WEB_SERVICE', ('SOAP Web Service')
        QUEUE = 'QUEUE', ('Queue')
        FILE_TRANSFER = 'FILE_TRANSFER', ('File Transfer')
        
    implementation_type = models.CharField(
        max_length=20,
        choices=ImplementationTypeEnum.choices,
        default=ImplementationTypeEnum.API,
    )   


    def __str__(self):
        return f"{self.interface.interface_id}-{self.implementation_type}-{self.implementation_counter}"