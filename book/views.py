from django.shortcuts import render
from .models import Book

def boards_home(request):
    books = Book.objects.all()
    return render(request, 'boards_home.html', {'books': books})



# Create your views here.
