from django.shortcuts import render
from pattern.models import Pattern
from django.views.generic import ListView

# Create your views here.
class SearchView(ListView):
    model = Pattern
    template_name = 'search.html'