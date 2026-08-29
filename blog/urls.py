from django.urls import path
from .views import *
app_name = "blog"

urlpatterns = [
    path("", blog_home, name="home"),
    path("<int:pid>/", blog_single , name ="single"),
    path("category/<str:cat>",blog_home, name="category"),
    path("tag/<str:tag>",blog_home, name="tag"),
    path("serach/",blog_home , name ="search"),
]