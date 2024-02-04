from django.urls import path
from . import views
from .views import ProfileView

app_name = 'profiles'

urlpatterns = [
    path("<str:username>/", views.ProfileView.as_view(), name='profile'),
    path("<str:username>/edit/", views.edit_profile, name='edit'),
]