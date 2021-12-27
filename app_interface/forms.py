from django import forms
from app_interface.models import Interface

class InterfaceForm(forms.ModelForm):
    class Meta:
        model = Interface
        fields = ['interface', 'status']
