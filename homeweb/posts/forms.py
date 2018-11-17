from django import forms
from .models import Post, Image, Comment

# 게시물 작성, Post & Images
class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=50, label='제목')
    img = forms.ImageField(label='썸네일')
    content = forms.CharField(max_length=80, label='내용')

    class Meta:
        model = Post
        fields = ['title', 'img', 'content', 'user']

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='사진')

    class Meta:
        model = Image
        fields = ['image', ]

class CommentForm(forms.Form):
    content = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'content',
                'placeholder': '댓글',
            }
        )
    )

    def clean_content(self):
        data = self.cleaned_data['content']
        errors = []
        if data == '':
            errors.append(forms.ValidationError('댓글 내용을 입력해주세요'))
        elif len(data) > 50:
            errors.append(forms.ValidationError('댓글 내용은 50자 이하로 입력해주세요'))
        if errors:
            raise forms.ValidationError(errors)
        return data
