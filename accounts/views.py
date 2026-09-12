from django.shortcuts import render , HttpResponse , redirect
from .forms import SignupForm 
from django.contrib.auth import login , logout 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth.views import PasswordResetView , PasswordResetConfirmView 
from django.urls import reverse_lazy

def signup(request):
    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
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
        form = AuthenticationForm(request=request,data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request, f"congratulations .{user}  login  successfully ")
            return redirect('pages:home')
        else:
            messages.error(request, 'Invalid login.')
            messages.error(request, form.errors)
            return redirect('accounts:login')

    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request,'accounts/login.html',context)

@login_required
def logout_page(request):
    logout(request)
    return redirect('pages:home')
# Create your views here.

class CustomPasswordResetView(PasswordResetView):
    success_url = reverse_lazy('accounts:password_reset_done')

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('accounts:password_reset_complete')