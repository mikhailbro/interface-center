from django import forms
from app_implementation.models import Implementation


class ImplementationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(ImplementationForm, self).__init__(*args, **kwargs)
       self.fields['interface'].widget.attrs['readonly'] = True
       self.fields['technology_type'].widget.attrs['readonly'] = True
       self.fields['provider_counter'].widget.attrs['readonly'] = True
       
    class Meta:
        model = Implementation
        fields = ['interface', 'provider', 'technology_type', 'delivery_address', 'provider_counter', 'artefact_url', 'consumers']
        