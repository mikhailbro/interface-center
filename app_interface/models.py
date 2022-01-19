import datetime
from django.db import models
from django.contrib.auth.models import User
from app_application.models import Application

# Create your models here.
class Interface(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    owner_application = models.ForeignKey(Application, on_delete=models.DO_NOTHING, default=None)
    interface_id = models.CharField(max_length=31, default='wird vom Tool vergeben', verbose_name='Interface ID')
    name = models.CharField(max_length=100)
    version = models.PositiveIntegerField(default=1)
    description = models.TextField(max_length=500, default='')
    owned_interface = models.BooleanField(default=True)
    created_at = models.DateField(default=datetime.date.today)
    production_start_at = models.DateField(default=datetime.date.today)
    decommissioning_at = models.DateField(null=True, blank=True, default=None)
    multi_provider = models.BooleanField(default=False)
    contract_description = models.URLField(max_length=200, verbose_name='Interface Contract URL', null=True, blank=True, default=None)
    
    restriction = models.BooleanField(default=False)
    restriction_text = models.TextField(max_length=300, null=True, blank=True, default=None)
    
    restriction_code_choices = [('NUTZUNG', 'NUTZUNG'), ('TEST', 'TEST')]
    restriction_code = models.CharField(max_length=20, choices=restriction_code_choices, blank=True, null=True, default=None)

    status_choices=[('EINGANG', 'Eingang'), ('ENTWICKLUNG', 'Entwicklung'), ('TEST', 'Test'), ('PRODUKTION', 'Produktion'), ('RUECKZUG', 'Rueckzug'), ('HISTORISCH', 'Historisch'), ('ABGELEHNT', 'Abgelehnt')]
    status = models.CharField( max_length=32, choices=status_choices, default='EINGANG')

    model_origin_choices=[('','---------'), ('CODE', 'Code'), ('CONTRACT', 'Contract'), ('MODEL', 'Model')]
    model_origin = models.CharField(max_length=10,choices=model_origin_choices, default=None)

    info_classification_choices=[('','---------'), ('PUBLIC', 'Public'), ('INTERNAL', 'Internal'), ('CONFIDENTIONAL', 'Confidentional'), ('SECRET', 'Secret')]
    info_classification = models.CharField(max_length=20, choices=info_classification_choices, default=None)

    infoflow_direction_choices=[('','---------'), ('TO_PROVIDER', 'To Provider'), ('FROM_PROVIDER', 'From Provider'), ('BOTH_DIRECTIONS', 'Both Directions')]
    infoflow_direction = models.CharField(max_length=20, choices=infoflow_direction_choices, default=None)

    accessibility_choices=[('','---------'), ('DOMAIN_INTERNAL', 'Domain internal'), ('CROSS_DOMAIN', 'Cross domain')]
    accessibility = models.CharField(max_length=20, choices=accessibility_choices, default=None)

    communication_pattern_choices=[('','---------'), ('REQUEST_REPLY', 'Request-Reply'), ('FIRE_FORGET', 'Fire-Forget')]
    communication_pattern = models.CharField(max_length=20, choices=communication_pattern_choices, default=None)

    interface_type_choices=[('','---------'), ('API', 'API'), ('WEB_SERVICE', 'SOAP Web Service'), ('QUEUE', 'Queue'), ('FILE_TRANSFER', 'File Transfer')]
    interface_type = models.CharField(max_length=20, choices=interface_type_choices, default=None) 


    business_domain_choices=[('','---------'),
                                ('A.1 ACME Core', '-A.1 ACME Core'), 
                                ('A.2 ACME Partner', '- A.2 ACME Partner'), ('A.2.1 ACME Partner Address', '-- A.2.1 ACME Partner Address'), ('A.2.3 ACME Partner Contact', '-- A.2.3 ACME Partner Contact'), 
                                ('B.1 ACME Contract', '- B.1 ACME Contract'), 
                                ('B.2 ACME Offer', '- B.2 ACME Offer'), ('B.2.1 ACME Offer Campaign', '-- B.2.1 ACME Offer Campaign'),
                                ('C.1 ACME Finance', '- C.1 ACME Finance'), 
                                ('C.2 ACME Legal & Compliance', '- C.2 ACME Legal & Compliance'), ('C.2.1 ACME Legal', '-- C.2.1 ACME Legal'), ('C.2.2 ACME Compliance', '-- C.2 ACME Compliance'),
                                ('D.1 ACME Purchasing', '- D.1 ACME Purchasing')]
    business_domain = models.CharField(max_length=50, choices=business_domain_choices)


    def __str__(self):
        return self.name + " (" + self.interface_id + ")"
