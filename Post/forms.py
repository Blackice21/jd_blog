from django import forms
from .models import Post_m

class PostForm(forms.ModelForm):
    class Meta:
        model = Post_m
        fields = ('__all__')