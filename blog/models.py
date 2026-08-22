from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    counted_view = models.IntegerField(default=0)
    published_date = models.DateField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.title
   
   # image = models.ImageField(blank=True ,upload_to='images')
    #category 
    #tags


# Create your models here.
