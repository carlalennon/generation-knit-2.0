"""
URL configuration for gknit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import path, include, re_path

# App URLS
from feed import urls as feed_urls
from pattern import urls as pattern_urls
from profiles import urls as profile_urls

urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path('admin/', admin.site.urls),
    path('', include(feed_urls), name='feed'),
    path('', include(pattern_urls), name='patterns'),
    path('profile/', include(profile_urls), name='profile'),
    path("accounts/", include("allauth.urls"), name='accounts'),
    path('search/', include('search.urls'), name='search'),
    re_path('', include("allauth.urls"))
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
