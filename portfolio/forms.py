from django import forms
from .models import UserProfile

class Person_form(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['Name', 'password']