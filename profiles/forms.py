from django import forms
from django_summernote.widgets import SummernoteWidget
from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile

class EditProfile(forms.ModelForm):
    image = forms.FileField(required=False)
    bio = forms.CharField(widget=SummernoteWidget)

    class Meta:
        model = Profile
        fields = [ 'image', 'bio']