from django import forms
from .models import Commenttt

class CommentForm(forms.ModelForm):
    class Meta:
        model = Commenttt
        fields = [ 'text']
        widgets = {
            
            'text': forms.Textarea(attrs={'placeholder': 'Your comment'}),
        }
        