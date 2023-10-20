from django.contrib import admin

from .models import Book


@admin.register(Book)
class UserAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'genre']
