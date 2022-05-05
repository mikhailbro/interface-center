import datetime
from django.db import models
from django.contrib.auth.models import User
from app_application.models import Application

# Create your models here.
class Interface(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    owner_application = models.ForeignKey(Application, on_delete=models.DO_NOTHING, default=None)
    
    interface_id = models.CharField(max_length=31, default='wird vom Tool vergeben', verbose_name='Interface ID')
    major_version = models.PositiveIntegerField(default=1)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, default='')
    owned_interface = models.BooleanField(default=True)
    doc_link = models.URLField(max_length=200, verbose_name='Doc Link', null=True, blank=True, default=None)
    workend_date = models.DateField(null=True, blank=True, default=None)
    
    restriction = models.BooleanField(default=False)
    restriction_text = models.CharField(max_length=150, null=True, blank=True, default=None)
    
    restriction_code_choices = [('NUTZUNG', 'NUTZUNG'), ('TEST', 'TEST')]
    restriction_code = models.CharField(max_length=20, choices=restriction_code_choices, blank=True, null=True, default=None)

    status_choices=[('EINGANG', 'Eingang'), ('ENTWICKLUNG', 'Entwicklung'), ('TEST', 'Test'), ('PRODUKTION', 'Produktion'), ('RUECKZUG', 'Rueckzug'), ('HISTORISCH', 'Historisch'), ('ABGELEHNT', 'Abgelehnt')]
    status = models.CharField( max_length=32, choices=status_choices, default='EINGANG')

    info_classification_choices=[('','---------'), ('PUBLIC', 'Public'), ('INTERNAL', 'Internal'), ('CONFIDENTIONAL', 'Confidentional'), ('SECRET', 'Secret')]
    info_classification = models.CharField(max_length=20, choices=info_classification_choices, default=None)

    infoflow_direction_choices=[('','---------'), ('TO_PROVIDER', 'To Provider'), ('FROM_PROVIDER', 'From Provider'), ('BOTH_DIRECTIONS', 'Both Directions')]
    infoflow_direction = models.CharField(max_length=20, choices=infoflow_direction_choices, default=None)

    domain_name_choices=[('','---------'),
                                ('A.1 ACME Core', '-A.1 ACME Core'), 
                                ('A.2 ACME Partner', '- A.2 ACME Partner'), ('A.2.1 ACME Partner Address', '-- A.2.1 ACME Partner Address'), ('A.2.3 ACME Partner Contact', '-- A.2.3 ACME Partner Contact'), 
                                ('B.1 ACME Contract', '- B.1 ACME Contract'), 
                                ('B.2 ACME Offer', '- B.2 ACME Offer'), ('B.2.1 ACME Offer Campaign', '-- B.2.1 ACME Offer Campaign'),
                                ('C.1 ACME Finance', '- C.1 ACME Finance'), 
                                ('C.2 ACME Legal & Compliance', '- C.2 ACME Legal & Compliance'), ('C.2.1 ACME Legal', '-- C.2.1 ACME Legal'), ('C.2.2 ACME Compliance', '-- C.2 ACME Compliance'),
                                ('D.1 ACME Purchasing', '- D.1 ACME Purchasing')]
    domain_name = models.CharField(max_length=50, choices=domain_name_choices)


    def __str__(self):
        return self.name + " (" + self.interface_id + ")"
