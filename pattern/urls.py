from . import views
from django.urls import path
from .views import UploadPatternView

app_name = "pattern"

urlpatterns = [
    path('', views.PatternView.as_view(), name="pattern"),
    path('add/', UploadPatternView.as_view(), name="add"),
]