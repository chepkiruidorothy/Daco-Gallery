
# Create your views here.
from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm
from photo_site.models import Category
# Create your views here.
def blog(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    return render(request,'blog.html',{'posts':posts,'categories':categories})

def new_post(request):
    categories = Category.objects.all()
    if request.method=="POST":
        form = PostForm(request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('home')
    else:
        form=PostForm()
    return render(request, "new_post.html", {'form':form,'categories':categories})

def post_details(request,slug):
    categories = Category.objects.all()
    post=Post.objects.get(slug=slug)
    comments=Comment.objects.order_by("-created_on")
    new_comment=None
    if request.method=="POST":
        form = CommentForm(request.POST or None)
        if form.is_valid():
            new_comment= form.save(commit=False)
            new_comment.post=post

            new_comment.save()
            return render(request, "add_comment.html")
    else:
        form=CommentForm()
    return render(request, "add_comment.html", { 'form': form ,'post':post, 'comments':comments,'new_comment':new_comment,'categories':categories})

def delete_post(request, slug):
    post=Post.objects.get(slug=slug)
    if request.method == "POST":
        post.delete()
        return redirect("home")
    return render(request, 'delete.html', {'post':post})
