from django.shortcuts import render ,HttpResponse , redirect
from blog.models import Post , Category , Tag
from .forms import ContactForm
from django.contrib import messages
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
            form.save()
            messages.success(request, "your submit is successfully ")
            return redirect('pages:contact')
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
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
