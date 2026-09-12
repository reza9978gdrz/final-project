from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db.models import Q
from django.contrib.auth import get_user_model ,authenticate
from django.contrib.auth.backends import ModelBackend

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
#---------------------------------------------------------------------
class UsernameOrEmail(ModelBackend):
    def authenticate(self, request, username = None, password = None, **kwargs):
        if username is None or password is None:
            return 
        UserModel = get_user_model()
        
        try:
            user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))

            if  self.user_can_authenticate(user) and user.check_password(password):
                return user

        except UserModel.DoesNotExist:
            return None
