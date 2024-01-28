from django.shortcuts import render
from django.views import generic
from .models import Pattern
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import TemplateView, DetailView, FormView
from .forms import PostPattern

# Create your views here.
class PatternView(generic.ListView):
    queryset = Pattern.objects.all()
    template_name = "pattern/index.html"
    paginate_by = 3

def patterns(request):
    myPatterns = Pattern.objects.all()
    template = loader.get_template('index.html')
    context = {
        'myPatterns' : myPatterns,
    }
    return HttpResponse(template.render(context, request))

class UploadPatternView(FormView):
    template_name = "new_pattern.html"
    form_class = PostPattern
    success_url = "/"

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # Create a new pattern
        new_object = Pattern.objects.create(
            title = form.cleaned_data["title"],
            image = form.cleaned_data["image"]
        )
        messages.add_message(self.request, messages.SUCCESS, 'Post successful')
        return super().form_valid(form)