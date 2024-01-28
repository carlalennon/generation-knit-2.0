from . import views
from django.urls import path

urlpatterns = [
    path('pattern/', views.PatternView.as_view(),),
    path('add/', UploadPatternView.as_view(), name="add"),
]