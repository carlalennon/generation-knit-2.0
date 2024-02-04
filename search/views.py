from django.shortcuts import render
from pattern.models import Pattern
from django.views.generic import ListView

# Create your views here.
class SearchView(ListView):
    model = Pattern
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('p')
        pattern_search = Pattern.objects.filter(
            Q(name__icontains=query)
        )
        return pattern_search
    