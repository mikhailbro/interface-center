from django import forms

from app_interface.models import Interface


class InterfaceActionsForm(forms.ModelForm):
    
    class Meta:
        model = Interface
        fields = ['name', 'interface_id', 'major_version', 'doc_link', 'description']
