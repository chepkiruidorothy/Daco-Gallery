from django.shortcuts import render, redirect
import random
from .models import *

# Create your views here.
GRID_SIZE = 16

def home(request):
    images = list(Gallery.objects.all())
    categories = Category.objects.all()
    if len(images) > GRID_SIZE:
        images = random.sample(images,GRID_SIZE)
    else:
        images = Gallery.objects.all()

    return render(request,'index.html',{'images':images,'categories':categories})

def about(request):
    categories = Category.objects.all()
    return render(request, 'about.html',{'categories':categories})


def category(request,slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug=slug)
    images = Gallery.objects.filter(category__slug = slug)

    return render(request,'category.html',{'categories':categories,'category':category,'images':images})

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request, 'contact.html')
