from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import DetailView
from .models import Profile
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
            return redirect('profiles:profile', pk=profile.pk)
    else:
        form = EditProfile(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})

"""
def delete_pattern(request, pk):
    pattern = get_object_or_404(Pattern, pk=pk)
    pattern.delete()
    messages.add_message(request, messages.SUCCESS, "Your pattern was deleted.")
    return redirect('feed:feed')
    """