from django.shortcuts import render ,HttpResponse
from blog.models import Post , Category , Tag
from .forms import ContactForm
import datetime as dt

def home(request):
    posts = Post.objects.filter(status=1, published_date__lte = dt.date.today())
    context = {'posts':posts }
    return render(request,'pages/index.html',context)

def about(request):
    return render(request,'pages/about.html')

def contact(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.clean_email)
            form.save()
            return HttpResponse('done')
    else:
        form = ContactForm()
    context = {'form':form}
    return render(request,'pages/contact.html',context)

def test(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            print(form.errors)
    else:
        form =ContactForm()
    context = {'form':form}
    return render(request,'pages/test.html',context)
# Create your views here.
