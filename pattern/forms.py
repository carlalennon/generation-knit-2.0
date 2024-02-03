from django import forms
from django_summernote.widgets import SummernoteWidget
from django.shortcuts import render, get_object_or_404, redirect
from .models import Pattern

class PostPattern(forms.Form):
    title = forms.CharField(max_length=200)
    image = forms.FileField(required=False)
    content = forms.CharField(widget=SummernoteWidget)

def edit_pattern(request, pattern_id):
    pattern = get_object_or_404(Pattern, id=pattern_id)
    if request.method == 'POST':
        form = PostPattern(request.POST, request.FILES, instance=pattern)
        if form.is_valid():
            form.save()
            return redirect('pattern_detail', pattern_id=pattern.id)
    else:
        form = PostPattern(instance=pattern)
    return render(request, 'edit_pattern.html', {'form': form})


