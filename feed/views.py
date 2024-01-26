from django.views.generic import TemplateView, DetailView, FormView
from .forms import PostPattern
from pattern.models import Pattern

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patterns'] = Pattern.objects.all().order_by('-id')
        return context

class PatternDetailView(DetailView):
    template_name = "pattern_detail.html"
    model = Pattern

class UploadPatternView(FormView):
    template_name = "new_pattern.html"
    form_class = PostPattern
    success_url = "/"

    def form_valid(self, form):
        # Create a new pattern
        new_object = Pattern.objects.create(
            title = form.cleaned_data["title"],
            image = form.cleaned_data["image"]
        )
        return super().form_valid(form)