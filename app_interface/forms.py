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
        fields = ['name', 'interface_id', 'owner', 'owner_application', 'status', 'major_version', 'doc_link', 'description', 'domain_name', 'owned_interface', 'workend_date', 'info_classification', 'infoflow_direction', 'restriction', 'restriction_code', 'restriction_text']

        widgets = {
            'workend_date':forms.SelectDateWidget(attrs={'style': 'display: inline-block; width: 33%;'})
        }
