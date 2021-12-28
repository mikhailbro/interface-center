from django import forms
from app_interface.models import Interface

class InterfaceForm(forms.ModelForm):
    class Meta:
        model = Interface
        fields = ['name', 'interface_id', 'status', 'version', 'description', 'owned_interface', 'created_at', 'production_start_at', 'decommissioning_at', 'model_origin', 'info_classification', 'infoflow_direction', 'accessibility', 'communication_pattern', 'multi_provider', 'contract_description', 'restriction', 'restriction_text', 'restriction_code']
