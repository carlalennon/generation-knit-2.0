from django.views.generic import TemplateView, DetailView, FormView, ListView
from pattern.models import Pattern
from django.contrib import messages

# Create your views here.

class HomePageView(ListView):
    template_name = 'home.html'
    model = Pattern
    context_object_name = 'patterns'
    paginate_by = 2  # Display 2 posts per page

    def get_queryset(self):
        return Pattern.objects.all().order_by('-id')

"""class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patterns'] = Pattern.objects.all().order_by('-id')

        #Paginator
        
        return context"""

class PatternDetailView(DetailView):
    template_name = "pattern_detail.html"
    model = Pattern

    def EditPattern(request):
        user = user.username
        pattern = pattern.author.username
        template = loader.get_template('pattern_detail.html')
        context = {
            'user': user,
            'pattern' : pattern,
            }
        return HttpResponse(template.render(context, request))

