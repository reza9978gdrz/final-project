from django.shortcuts import render , HttpResponse , redirect
from .forms import SignupForm , LoginForm
from django.contrib.auth import login , logout 
from django.contrib import messages

def signup(request):
    if request.method=='POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "congratulations . you signup  successfully ")
            return redirect('pages:home')
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
            return redirect('accounts:signup')

    else:
        form = SignupForm()
    context = {'form':form}
    return render(request,'accounts/signup.html',context)
#-----------------------------------------------------------------------------------------------------------

def login_page(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print('VALID')
            user = form.get_user()
            login(request,user)
            messages.success(request, f"congratulations .{user.name}  login  successfully ")
            return redirect('pages:home')
        else:
            print('inVALID')
            print(form.errors)

    else:
        form = LoginForm()
    context = {'form':form}
    return render(request,'accounts/login.html',context)


# Create your views here.
