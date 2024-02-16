from django import forms
from .models import UserRegistration

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = ['date', 'month', 'year', 'firstname', 'lastname', 'contact', 'email', 'username', 'password']
