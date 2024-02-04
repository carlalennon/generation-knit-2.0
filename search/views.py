from django.shortcuts import render
from pattern.models import Pattern
from django.views.generic import ListView
from django.db.models import Q

# Create your views here.
class SearchView(ListView):
    model = Pattern
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('p')
        pattern_search = Pattern.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
        return pattern_search
    