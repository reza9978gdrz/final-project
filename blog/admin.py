from django.contrib import admin
from .models import Post , Category  ,Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','status','created_date','counted_view','id')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','post','created_date','approved',)

admin.site.register(Category)
# Register your models here.
