from django import forms
from .models import Post, Image, Comment

# 게시물 작성, Post & Images
class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=50)
    content = forms.CharField(max_length=80)

    class Meta:
        model = Post
        fields = ['title', 'content', 'user']

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = Image
        fields = ['image', ]
