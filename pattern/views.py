from django.shortcuts import render
from django.views import generic
from .models import Pattern
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .forms import PostPattern
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class PatternView(generic.ListView):
    queryset = Pattern.objects.all()
    template_name = "pattern/index.html"
    paginate_by = 3


class UploadPatternView(LoginRequiredMixin, CreateView):
    model = Pattern
    template_name = 'new_pattern.html'
    fields = [
        'title',
        'content',
        'category',
        'weight',
        'needle',
        'image',
    ]
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)

