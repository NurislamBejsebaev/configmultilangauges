from django.contrib import admin
from .models import Reader, BookReading


@admin.register(Reader)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(BookReading)
class UserAdmin(admin.ModelAdmin):
    list_display = ['book', 'reader']
