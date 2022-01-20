from django import forms

from app_interface.models import Interface


class InterfaceActionsForm(forms.ModelForm):
    
    class Meta:
        model = Interface
        fields = ['name', 'interface_id', 'version', 'contract_description', 'description', 'created_at', 'production_start_at']

        widgets = {
            'created_at':forms.SelectDateWidget(attrs={'style': 'display: inline-block; width: 33%;'}),
            'production_start_at':forms.SelectDateWidget(attrs={'style': 'display: inline-block; width: 33%;'})
        }