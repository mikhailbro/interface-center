import datetime
from django.db import models
from django.contrib.auth.models import User
from app_application.models import Application


# Create your models here.
class Interface(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    owner_application = models.ForeignKey(Application, on_delete=models.DO_NOTHING, default=None)
    interface_id = models.CharField(max_length=10, default='', verbose_name='Interface ID')
    name = models.CharField(max_length=100)
    version = models.PositiveIntegerField(default=1)
    description = models.TextField(max_length=500, default='')
    owned_interface = models.BooleanField(default=True)
    created_at = models.DateField(default=datetime.date.today)
    production_start_at = models.DateField(default=datetime.date.today)
    decommissioning_at = models.DateField(null=True, blank=True, default=None)
    # business_domain = models.CharField(max_length=50)
    multi_provider = models.BooleanField(default=False)
    contract_description = models.URLField(max_length=200, verbose_name='Interface Contract URL', null=True, blank=True, default=None)
    
    restriction = models.BooleanField(default=False)
    restriction_text = models.TextField(max_length=300, null=True, blank=True, default=None)
    class RestrictionCodeEnum(models.TextChoices):
        NUTZUNG = 'NUTZUNG', ('Nutzung')
        TEST = 'TEST', ('Test')

    restriction_code = models.CharField(
        max_length=20,
        choices=RestrictionCodeEnum.choices,
        null=True, blank=True, default=None
    )

    class InterfaceStatusEnum(models.TextChoices):
        EINGANG = 'EINGANG', ('Eingang')
        ENTWICKLUNG = 'ENTWICKLUNG', ('Entwicklung')
        TEST = 'TEST', ('Test')
        PRODUKTION = 'PRODUKTION', ('Produktion')
        RUECKZUG = 'RUECKZUG', ('Rueckzug')
        HISTORISCH = 'HISTORISCH', ('Historisch')
        ABGELEHNT = 'ABGELEHNT', ('Abgelehnt')

    status = models.CharField(
        max_length=16,
        choices=InterfaceStatusEnum.choices,
        default=InterfaceStatusEnum.EINGANG,
    )

    class ModelOriginEnum(models.TextChoices):
        CODE = 'CODE', ('Code')
        CONTRACT = 'CONTRACT', ('Contract')
        MODEL = 'MODEL', ('Model')

    model_origin = models.CharField(
        max_length=10,
        choices=ModelOriginEnum.choices,
        default=ModelOriginEnum.CODE,
    )

    class InfoClassificationEnum(models.TextChoices):
        PUBLIC = 'PUBLIC', ('Public')
        INTERNAL = 'INTERNAL', ('Internal')
        CONFIDENTIONAL = 'CONFIDENTIONAL', ('Confidentional')
        SECRET = 'SECRET', ('Secret')

    info_classification = models.CharField(
        max_length=20,
        choices=InfoClassificationEnum.choices,
        default=InfoClassificationEnum.INTERNAL,
    )

    class InfoflowDirectionEnum(models.TextChoices):
        TO_PROVIDER = 'TO_PROVIDER', ('To Provider')
        FROM_PROVIDER = 'FROM_PROVIDER', ('From Provider')
        BOTH_DIRECTIONS = 'BOTH_DIRECTIONS', ('Both Directions')

    infoflow_direction = models.CharField(
        max_length=20,
        choices=InfoflowDirectionEnum.choices,
        default=InfoflowDirectionEnum.BOTH_DIRECTIONS,
    )

    class AccessibilityEnum(models.TextChoices):
        DOMAIN_INTERNAL = 'DOMAIN_INTERNAL', ('Domain internal')
        CROSS_DOMAIN = 'CROSS_DOMAIN', ('Cross domain')

    accessibility = models.CharField(
        max_length=20,
        choices=AccessibilityEnum.choices,
        default=AccessibilityEnum.DOMAIN_INTERNAL,
    )

    class CommunicationPatternEnum(models.TextChoices):
        REQUEST_REPLY = 'REQUEST_REPLY', ('Request-Reply')
        FIRE_FORGET = 'FIRE_FORGET', ('Fire-Forget')

    communication_pattern = models.CharField(
        max_length=20,
        choices=CommunicationPatternEnum.choices,
        default=CommunicationPatternEnum.REQUEST_REPLY,
    )


    def __str__(self):
        return self.name + "- " + self.status
