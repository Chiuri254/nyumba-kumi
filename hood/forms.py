from .models import Business,Profile
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']

class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        exclude=['owner','neighbourhood']