from django import forms

class UploadPostForm(forms.Form):
    title = forms.CharField(max_length=50)
    image = forms.FileField()
    content = forms.CharField(max_length=80)
