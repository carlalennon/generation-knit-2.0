from . import views
from django.urls import path

urlpatterns = [
    path('pattern/', views.PatternView.as_view(),),
]