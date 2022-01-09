from django import forms
from app_interface.models import Interface
from app_application.models import Application
from app_implementation.models import Implementation


class ImplementationForm(forms.ModelForm):
    class Meta:
        model = Implementation
        fields = ['interface', 'provider', 'implementation_type', 'provider_basepath', 'implementation_counter']