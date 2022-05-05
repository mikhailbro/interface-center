from django import forms
from app_application.models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['app_id', 'short_name', 'mail_address', 'status']
