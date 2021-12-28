from django import forms
from app_interface.models import Interface
from app_interface.models import Application
from app_interface.models import InterfaceImplentation

class InterfaceForm(forms.ModelForm):
    class Meta:
        model = Interface
        fields = ['name', 'interface_id', 'status', 'version', 'description', 'owned_interface', 'created_at', 'production_start_at', 'decommissioning_at', 'model_origin', 'info_classification', 'infoflow_direction', 'accessibility', 'communication_pattern', 'multi_provider', 'contract_description', 'restriction', 'restriction_text', 'restriction_code']


class Application(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['app_id', 'short_name', 'mail_address']


class InterfaceImplentation(forms.ModelForm):
    class Meta:
        model = InterfaceImplentation
        fields = ['interface', 'implementation_type', 'provider', 'provider_basepath', 'implementation_counter']