
from django.urls import path
from .views import HomePageView, PatternDetailView

app_name = 'feed'

urlpatterns = [
    path('', HomePageView.as_view(), name='feed'),
    path('pattern/<int:pk>/', PatternDetailView.as_view(), name="detail"),
]