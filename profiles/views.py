from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView
from django.contrib import messages
from .models import Profile
from pattern.models import Pattern
from .forms import EditProfile

# Create your views here.

class ProfileView(DetailView):
    http_method_names = ['get']
    template_name = 'profile.html'
    model = User
    context_object_name = 'user'
    slug_field = 'username'
    slug_url_kwarg = 'username'

def edit_profile(request, username):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Profile was edited successfully.")
            return redirect('profiles:profile', username=request.user)
    else:
        form = EditProfile(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})


def delete_profile(request, username):
    profile = get_object_or_404(Profile, user.username)
    user = get_object_or_404(User, user=request.user)
    profile.delete()
    user.delete()
    messages.add_message(request, messages.SUCCESS, "Your profile was deleted.")
    return redirect('feed:feed')

"""
class PatternsByUser(ListView):

    def get(self, request, *args, **kwargs):
        username = self.kwargs['username']
        profile = get_object_or_404(Profile, user__username=username)
        patterns = Pattern.objects.filter(author=profile.user)
        return render(request, 'profile.html', {'profile': profile, 'patterns': patterns})
"""    