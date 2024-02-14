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
        needle_size = self.request.GET.get('needle')
        category = self.request.GET.get('category')
        weight = self.request.GET.get('weight')

        if query is not None:
            patterns = Pattern.objects.filter(
                Q(title__icontains=query) | Q(author__username__icontains=query) | Q(content__icontains=query)
            )
        else:
            patterns = Pattern.objects.none()

        if needle_size:
            patterns = patterns.filter(needle_size=needle_size)

        if category:
            patterns = patterns.filter(category=category)

        if weight:
            patterns = patterns.filter(weight=weight)

        return patterns
    