from django import forms
from .models import BlogPost


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'content']

    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get('title')
    #     quryset = BlogPost.objects.filter(title=title)

    #     if quryset.exists():
    #         raise forms.ValidationError("this title already has exists \n please change your title")
        
    #     return title