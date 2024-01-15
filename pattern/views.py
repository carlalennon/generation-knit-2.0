from django.shortcuts import render
from django.views import generic
from .models import Pattern
from django.http import HttpResponse

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