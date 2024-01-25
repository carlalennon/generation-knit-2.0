from django.views.generic import TemplateView, DetailView, FormView
from .forms import PostForm
from pattern.models import Pattern

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patterns'] = Pattern.objects.all()
        return context

class PatternDetailView(DetailView):
    template_name = "pattern_detail.html"
    model = Pattern

class UploadPatternView(FormView):
    template_name = "new_pattern.html"
    form_class = PostForm
    success_url = "/"