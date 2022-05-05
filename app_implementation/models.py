from django.db import models
from app_interface.models import Interface
from app_application.models import Application



# Create your models here.
class Implementation(models.Model):
    interface = models.ForeignKey(Interface, on_delete=models.CASCADE, default=None)
    provider = models.ForeignKey(Application, on_delete=models.DO_NOTHING, default=None, related_name='provider')
    consumers = models.ManyToManyField(Application, blank=True, related_name='consumers')

    delivery_address = models.CharField(max_length=100, default='')
    provider_counter = models.CharField(max_length=23, default='wird vom Tool vergeben')

    technology_type_choices = [('API', 'API'), ('WEB_SERVICE', 'SOAP Web Service'), ('QUEUE', 'Queue'), ('FILE_TRANSFER', 'File Transfer')]
    technology_type = models.CharField(max_length=20, choices=technology_type_choices, default='API')   

    artefact_url = models.URLField(max_length=200, verbose_name='Artefact URL', null=True, blank=True, default=None)


    def __str__(self):
        return f"{self.interface.interface_id}-{self.technology_type}-{self.provider}-{self.provider_counter}"