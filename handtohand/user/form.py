from django import forms
from .models import User

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'nickname', 'date_of_birth', 'address']
