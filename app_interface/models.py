from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Interface(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    interface = models.CharField(max_length=300)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.interface + "- " + str(self.status)