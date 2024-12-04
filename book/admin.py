from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'fecha_creacion', 'fecha_modificacion')


# Register your models here.
