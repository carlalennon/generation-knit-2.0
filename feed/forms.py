from django import forms

class PostPattern(forms.Form):
    title = forms.CharField(max_length=200)
    image = forms.FileField()
