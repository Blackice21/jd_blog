from django import forms
from .models import Post_m, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post_m
        fields = ('__all__')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']