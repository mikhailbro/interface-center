from django import forms
from django.forms import HiddenInput

from app_interface.models import Interface


class InterfaceForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
       super(InterfaceForm, self).__init__(*args, **kwargs)
       self.fields['interface_id'].widget.attrs['readonly'] = True
       self.fields['owner'].widget.attrs['readonly'] = True
       self.fields['status'].widget.attrs['readonly'] = True
       #self.fields['interface_id'].widget = HiddenInput()

    class Meta:
        model = Interface
        fields = ['name', 'interface_id', 'owner', 'owner_application', 'status', 'version', 'contract_description', 'description', 'interface_type', 'business_domain', 'owned_interface', 'created_at', 'production_start_at', 'decommissioning_at', 'multi_provider', 'interface_origin', 'info_classification', 'infoflow_direction', 'accessibility', 'communication_pattern', 'restriction', 'restriction_code', 'restriction_text']

        widgets = {
            'created_at':forms.SelectDateWidget(attrs={'style': 'display: inline-block; width: 33%;'}),
            'production_start_at':forms.SelectDateWidget(attrs={'style': 'display: inline-block; width: 33%;'}),
            'decommissioning_at':forms.SelectDateWidget(attrs={'style': 'display: inline-block; width: 33%;'})
        }
