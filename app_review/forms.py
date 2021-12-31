from django import forms
from app_interface.models import Interface
from app_application.models import Application
from app_review.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['interface']