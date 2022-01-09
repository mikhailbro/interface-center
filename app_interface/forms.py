from django import forms
from app_interface.models import Interface


class InterfaceForm(forms.ModelForm):
    class Meta:
        model = Interface
        fields = ['name', 'interface_id', 'owner', 'owner_application', 'status', 'version', 'description', 'owned_interface', 'created_at', 'production_start_at', 'decommissioning_at', 'model_origin', 'info_classification', 'infoflow_direction', 'accessibility', 'communication_pattern', 'multi_provider', 'contract_description', 'restriction', 'restriction_text', 'restriction_code']

        widgets = {
            'created_at':forms.SelectDateWidget(attrs={'style': 'display: inline-block; width: 33%;'}),
            'production_start_at':forms.SelectDateWidget(attrs={'style': 'display: inline-block; width: 33%;'}),
            'decommissioning_at':forms.SelectDateWidget(attrs={'style': 'display: inline-block; width: 33%;'})
        }
