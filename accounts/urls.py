from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
app_name = "accounts"

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", login_page , name ="login"),
    path("logout/", logout_page , name ="logout"),
     path('password-reset/',
         CustomPasswordResetView.as_view(
             template_name='registration/password_reset_form.html'
         ),
         name='password_reset'),
     
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'
         ),
         name='password_reset_done'),
     
    path('reset/<uidb64>/<token>/',
         CustomPasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
     
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]