from django.shortcuts import render
from django.views import generic
from .models import Pattern

# Create your views here.
class PatternView(generic.ListView):
    model = Pattern