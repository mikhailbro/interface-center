from django import forms
from app_review.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['interface', 'review_name', 'requestor', 'reviewer', 'review_status', 'created_at', 'findings']