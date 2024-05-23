from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['email', 'text']
        widgets = {
            # 'email': forms.Textarea(attrs={'placeholder':'for example emailname@gmail.com'}),
            'text': forms.Textarea(attrs={'placeholder':'write your comment'}),
        }
    
