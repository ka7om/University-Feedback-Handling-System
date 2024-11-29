from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['topic', 'message']  # Fields to include in the form
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }
