from django.shortcuts import render

def blog_home(request):
    return render(request,'blog/blog_home.html')

def blog_single(request):
    return render(request,'blog/blog_category.html')
# Create your views here.
