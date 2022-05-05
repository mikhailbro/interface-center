import datetime
from django.db import models

# Create your models here.
class Interface_Actions(models.Model):
    interface_id = models.CharField(max_length=31, default='wird vom Tool vergeben', verbose_name='Interface ID')
    name = models.CharField(max_length=100)
    version = models.PositiveIntegerField(default=1)
    description = models.TextField(max_length=500, default='')
    doc_link = models.URLField(max_length=200, verbose_name='Doc Link', null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.name} ({self.interface_id})"
