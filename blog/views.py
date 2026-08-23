from django.shortcuts import render
from .models import Post

def blog_home(request):
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request,'blog/blog_home.html',context)

def blog_single(request):
    return render(request,'blog/blog_category.html')
# Create your views here.
