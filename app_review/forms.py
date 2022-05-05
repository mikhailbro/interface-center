from django import forms
from app_review.models import Review


class ReviewForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
       super(ReviewForm, self).__init__(*args, **kwargs)
       self.fields['interface'].widget.attrs['readonly'] = True
       self.fields['requestor'].widget.attrs['readonly'] = True
       self.fields['created_at'].widget.attrs['readonly'] = True
       
    class Meta:
        model = Review
        fields = ['interface', 'status', 'requestor', 'reviewer', 'created_at', 'findings']
        
        widgets = {
            'created_at':forms.SelectDateWidget(attrs={'style': 'display: inline-block; width: 33%;'})
        }
