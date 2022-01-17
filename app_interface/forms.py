from django import forms
from django.forms import HiddenInput

from app_interface.models import Interface


class InterfaceForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
       super(InterfaceForm, self).__init__(*args, **kwargs)
       self.fields['interface_id'].widget.attrs['readonly'] = True
       #self.fields['interface_id'].widget = HiddenInput()

    class Meta:
        model = Interface
        fields = ['name', 'interface_id', 'owner', 'owner_application', 'status', 'version', 'contract_description', 'description', 'interface_type', 'owned_interface', 'created_at', 'production_start_at', 'decommissioning_at', 'model_origin', 'info_classification', 'infoflow_direction', 'accessibility', 'communication_pattern', 'multi_provider', 'restriction', 'restriction_text', 'restriction_code']

        widgets = {
            'created_at':forms.SelectDateWidget(attrs={'style': 'display: inline-block; width: 33%;'}),
            'production_start_at':forms.SelectDateWidget(attrs={'style': 'display: inline-block; width: 33%;'}),
            'decommissioning_at':forms.SelectDateWidget(attrs={'style': 'display: inline-block; width: 33%;'})
        }
