from django.shortcuts import render, redirect
import random
from .models import Category, Shoot, Gallery

from .forms import EmailForm
from django.conf import settings
from django.core.mail import send_mail
from CMS.models import ImageField
# Create your views here.
GRID_SIZE = 16

def home(request):
    images = Gallery.objects.filter(featured=True).all()
    categories = Category.objects.all()
    cover_image = ImageField.objects.get(name = 'cover image')
    if len(images) > GRID_SIZE:
        images = random.sample(images,GRID_SIZE)
    else:
        images = images

    return render(request,'index.html',{'images':images,'categories':categories, 'cover_image':cover_image})

def about(request):
    categories = Category.objects.all()
    return render(request, 'about.html',{'categories':categories})


def category(request,slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug=slug)
    images = Gallery.objects.filter(category__slug = slug)

    return render(request,'category.html',{'categories':categories,'category':category,'images':images})

def services(request):
    categories = Category.objects.all()
    return render(request,'services.html',{'categories':categories})

def contact(request):
    categories = Category.objects.all()
    return render(request, 'contact.html',{'categories':categories})

# def blog(request):
#     blogs = Blog.objects.all()
#     return render(request, 'blog.html',{'blog':blog})
