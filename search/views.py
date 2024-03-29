from django.shortcuts import render
from pattern.models import Pattern
from django.views.generic import ListView
from django.db.models import Q

class SearchView(ListView):
    model = Pattern
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('p')
        needle = self.request.GET.get('needle')
        category = self.request.GET.get('category')
        weight = self.request.GET.get('weight')
        paginate_by = 8

        # Is not None means that page will still render when no query is entered 
        if query is not None:
            patterns = Pattern.objects.filter(
                # Searches title, author and content body for a match
                Q(title__icontains=query) | Q(author__username__icontains=query) | Q(content__icontains=query)
            )
        else:
            patterns = Pattern.objects.none()

        # Pattern filters
        if needle is not None and needle.isdigit():
            patterns = patterns.filter(needle=int(needle))

        if category is not None and category.isdigit():
            patterns = patterns.filter(category=int(category))

        if weight is not None and weight.isdigit():
            patterns = patterns.filter(weight=int(weight))

        return patterns
    