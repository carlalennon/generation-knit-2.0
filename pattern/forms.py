from django import forms
from django_summernote.widgets import SummernoteWidget
from django.shortcuts import render, get_object_or_404, redirect
from .models import Pattern

class PostPattern(forms.ModelForm):
    title = forms.CharField(max_length=200)
    image = forms.FileField(required=False)
    content = forms.CharField(widget=SummernoteWidget)