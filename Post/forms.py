from django import forms
from django.forms import widgets
from django.http import HttpRequest, request
from .models import Post_m, Comment, User


class PostForm(forms.ModelForm): 
    class Meta:
        model = Post_m
        fields = ('__all__')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['author'].widget = forms.HiddenInput()




class CommentForm(forms.ModelForm):
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows':4}))
    class Meta:
        model = Comment
        fields = ['content']