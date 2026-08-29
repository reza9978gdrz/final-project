from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    category = models.ForeignKey(Category ,on_delete=models.CASCADE , null=True)
    tag = models.ManyToManyField(Tag , null=True )
    counted_view = models.IntegerField(default=0)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now = True)
    
    class Meta():
        ordering = ['created_date']
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE , null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(null=True , blank=True)
       
    
    class Meta():
        ordering = ['-created_date']
    def __str__(self):
        return self.name
# Create your models here.
