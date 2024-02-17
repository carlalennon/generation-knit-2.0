from django.views.generic import TemplateView, DetailView, FormView, ListView
from pattern.models import Pattern
from django.contrib import messages

# List newest posts to generation knit in newest order
class HomePageView(ListView):
    template_name = 'home.html'
    model = Pattern
    context_object_name = 'patterns'
    paginate_by = 5  # Display 2 posts per page

    def get_queryset(self):
        return Pattern.objects.all().order_by('-id')


# Detailed view of pattern with all details
class PatternDetailView(DetailView):
    template_name = "pattern_detail.html"
    model = Pattern

    # Allow user to edit a pattern
    def EditPattern(request):
        user = user.username
        pattern = pattern.author.username
        template = loader.get_template('pattern_detail.html')
        context = {
            'user': user,
            'pattern' : pattern,
            }
        return HttpResponse(template.render(context, request))

