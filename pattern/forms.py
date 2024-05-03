from django import forms
from django_summernote.widgets import SummernoteWidget
from django.shortcuts import render, get_object_or_404, redirect
from .models import Pattern
from upload_validator import FileTypeValidator
from django.core.validators import FileExtensionValidator

# Allow user to upload a pattern
class PostPattern(forms.ModelForm):
    title = forms.CharField(max_length=200)
    # image validator from django
    image = forms.ImageField(
        required=False,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]
    )
    content = forms.CharField(widget=SummernoteWidget)
    # User can only upload PDFs to this field, using a different validator for more security 
    pdf = forms.FileField(
        label='pdf', help_text="Please upload a .pdf file", required=False,
        validators=[FileTypeValidator(
            allowed_types=['application/pdf'],
            allowed_extensions=[ '.pdf']
        )]
    )
    link_pattern = forms.CharField(required=False)
    category = forms.ChoiceField(choices=Pattern.CATEGORY, required=True)
    weight = forms.ChoiceField(choices=Pattern.WEIGHT, required=True)
    needle = forms.ChoiceField(choices=Pattern.NEEDLE, required=True)

    class Meta:
        model = Pattern
        fields = ['title', 'image', 'content', 'pdf', 'link_pattern', 'category', 'weight', 'needle']