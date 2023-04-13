"""
URL configuration for photosite project.

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
from django.urls import path,include
from photo_site import views

from django.conf.urls.static import static
from django.conf import settings

import blog
from blog import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    # path('contact/sendMail/', views.sendMail, name='sendMail'),
    # path('blog/', views.blog, name='blog'),
    path('category/<slug:slug>/', views.category, name='category'),
    path('blog/', include(blog.urls)),

]
if settings.DEBUG:
    urlpatterns= urlpatterns + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
