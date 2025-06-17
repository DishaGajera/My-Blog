from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Category, Post
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

admin.site.register(User, BaseUserAdmin)
admin.site.register(Category)
admin.site.register(Post)