from django import forms
from app_interface.models import Interface

class InterfaceForm(forms.ModelForm):
    class Meta:
        model = Interface
        fields = ['name', 'interface_id', 'version', 'description', 'is_owned', 'created_at', 'production_start_at', 'decommissioning_at', 'status', 'model_origin', 'info_classification', 'infoflow_direction']
