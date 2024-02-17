from django import forms
from django_summernote.widgets import SummernoteWidget
from django.shortcuts import render, get_object_or_404, redirect
from .models import Pattern
from upload_validator import FileTypeValidator

class PostPattern(forms.ModelForm):
    title = forms.CharField(max_length=200)
    image = forms.FileField(required=False)
    content = forms.CharField(widget=SummernoteWidget)
    pattern_pdf = forms.FileField(
        label='pdf', help_text="Please upload a .pdf file", required=False,
        validators=[FileTypeValidator(
            allowed_types=['application/pdf'],
            allowed_extensions=[ '.pdf']
        )]
    )
    link_pattern = forms.CharField(required=False)
        

    class Meta:
        model = Pattern
        fields = ['title', 'image', 'content', 'pattern_pdf', 'link_pattern']
