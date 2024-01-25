from django import forms

class PostForm(forms.Form):
    text = forms.Charfield()
    image = forms.FileField()