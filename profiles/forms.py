from django import forms
from django_summernote.widgets import SummernoteWidget
from django.shortcuts import render, get_object_or_404, redirect
from django.core.validators import FileExtensionValidator
from .models import Profile

# Allow user to edit their profile
class EditProfile(forms.ModelForm):
    image = forms.ImageField(
        required=False,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]
    )
    bio = forms.CharField(widget=SummernoteWidget)

    class Meta:
        model = Profile
        fields = [ 'image', 'bio']