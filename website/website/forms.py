from django import forms
from django.conf import settings

class LoginForm(forms.ModelForm):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ['username', 'password']
