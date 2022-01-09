from django import forms
from app_review.models import Review


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['interface', 'review_status', 'requestor', 'reviewer', 'created_at']
        
        widgets = {
            'created_at':forms.SelectDateWidget(attrs={'style': 'display: inline-block; width: 33%;'})
        }
