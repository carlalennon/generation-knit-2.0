from . import views
from django.urls import path

urlpatterns = [
    path('', views.PatternView.as_view(),),
]