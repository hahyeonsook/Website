from django import forms

class UploadPostForm(forms.Form):
    title = forms.CharField(max_length=50)
    image = forms.ImageField()
    content = forms.CharField(max_length=80)
