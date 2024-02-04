from django.shortcuts import render
from pattern.models import Pattern

# Create your views here.
class SearchVieww(ListView):
    model = Pattern
    template_name = 'search.html'