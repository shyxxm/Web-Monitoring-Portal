from django import forms
from django.forms import ModelForm
from .models import Website

#Create add url form

class UrlForm(ModelForm):
    class Meta:
        model = Website
        fields = "__all__"