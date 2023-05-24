from django.contrib import admin
from django.urls import path
from blog import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('', views.blog, name='blog'),
    path('<slug:slug>', views.post_details, name='post_details'),
    path('new_post/',views.new_post,name='new_post'),
    path('delete_blog_post/<slug:slug>/', views.delete_post, name='delete_blog_post'),
]

if settings.DEBUG:
    urlpatterns= urlpatterns + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
