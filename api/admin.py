from django.contrib import admin

# Register your models here.

from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff')
