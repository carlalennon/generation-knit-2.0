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
        needle = self.request.GET.get('needle')
        category = self.request.GET.get('category')
        weight = self.request.GET.get('weight')
        paginate_by = 8

        if query is not None:
            patterns = Pattern.objects.filter(
                Q(title__icontains=query) | Q(author__username__icontains=query) | Q(content__icontains=query)
            )
        else:
            patterns = Pattern.objects.none()

        if needle!= 'none':
            patterns = patterns.filter(needle=needle)

        if category != 'none':
            patterns = patterns.filter(category=category)

        if weight != 'none':
            patterns = patterns.filter(weight=weight)

        return patterns
    