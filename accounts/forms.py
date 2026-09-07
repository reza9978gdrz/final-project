from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import  AuthenticationForm

class SignupForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def clean_email(self):
        email_user = self.cleaned_data.get('email')
        user = User.objects.filter(email=email_user)
        if user.exists():
            raise forms.ValidationError('this email exist')
        else:
            return email_user

class LoginForm(AuthenticationForm):
    pass

