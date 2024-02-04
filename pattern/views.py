from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Pattern
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .forms import PostPattern
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages

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

def edit_pattern(request, pattern_id):
    pattern = get_object_or_404(Pattern, id=pattern_id)
    if request.method == 'POST':
        form = EditPattern(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Pattern was edited successfully.")
            return redirect('feed:detail', pk=pattern.pk)
    else:
        form = PostPattern(instance=pattern)
    return render(request, 'edit_pattern.html', {'form': form})

def delete_pattern(request, pk):
    pattern = get_object_or_404(Pattern, pk=pk)
    pattern.delete()
    messages.add_message(request, messages.SUCCESS, "Your pattern was deleted.")
    return redirect('feed:feed')
    