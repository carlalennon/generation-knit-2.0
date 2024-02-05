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
        if query is not None:
            pattern = Pattern.objects.filter(
                Q(title__icontains=query) | Q(author__username__icontains=query)
            )
        else:
            pattern = Pattern.objects.none()
        return pattern
    