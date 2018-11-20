from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=50)
    img = forms.ImageField()
    content = forms.CharField(max_length=80)

    class Meta:
        model = Post
        fields = ['title', 'image', 'content', 'user']

