from django.shortcuts import render
from .models import Book, Member, Transaction, Category

# Create your views here.

def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def index(request):
    return render(request, 'index.html')


def book_index(request):
    books = Book.objects.all()
    context = {'books': books}

    return render(request, 'books.html', context)


# Create your views here.
def index(request):
    return render(request, 'index.html')

