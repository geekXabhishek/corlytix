from django import forms
from .models import LoginCredential



class LoginForm(forms.ModelForm):
    class Meta:
        model = LoginCredential
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

