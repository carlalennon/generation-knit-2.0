from . import views
from django.urls import path
from .views import UploadPatternView

app_name = "pattern"

urlpatterns = [
    path('', views.PatternView.as_view(), name="pattern"),
    path('add/', UploadPatternView.as_view(), name="add"),
    path('edit/<int:pattern_id>/', views.edit_pattern, name="edit"),
    path('pattern/<int:pk>/remove/', views.delete_pattern, name="delete"),
]