from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ['name','email','created_date']

# Register your models here.
