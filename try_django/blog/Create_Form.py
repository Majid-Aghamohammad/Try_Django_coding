from django import forms
from .models import BlogPost


class CreateForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'content']
