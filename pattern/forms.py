from django import forms
from django_summernote.widgets import SummernoteWidget



class PostPattern(forms.Form):
    title = forms.CharField(max_length=200)
    image = forms.FileField(required=False)
    content = forms.CharField(widget=SummernoteWidget)
    #author = 


