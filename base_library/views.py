from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from base_library.forms import BookForm, MemberForm
from base_library.models import Book, Member
from users.forms import CustomUserCreationForm


# def register(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             # first_name = form.cleaned_data['first_name']
#             # last_name = form.cleaned_data['last_name']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password1']
#             user = authenticate(email=email, password=password)
#             login(request, user)
#             return redirect('home')
#
#         else:
#             return render(request, 'registration/register.html', {'form': form})
#
#     else:
#         form = CustomUserCreationForm()
#         return render(request, 'registration/register.html', {'form': form})
#
#
# def login_user(request):
#     if request.user.is_authenticated:
#         return redirect('book')
#
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST['password']
#         user = authenticate(request, email=email, password=password)
#         print(email, password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             form = AuthenticationForm()
#             return render(request, 'registration/login.html', {'form': form})
#
#     else:
#         form = AuthenticationForm()
#
#     context = {'form': form}
#     return render(request, 'registration/login.html', context)
#
#
# def logout_user(request):
#     logout(request)
#     return redirect('home')

@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def book_index(request):
    books = Book.objects.all()

    context = {'books': books}
    return render(request, 'books/book.html', context)

@login_required
def add_book(request):
    books = Book.objects.all()

    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('book')

    else:
        form = BookForm()
    context = {'books': books, 'form': form}

    return render(request, 'books/add_book.html', context)


@login_required
def update_book(request, pk):
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book')

    context = {'book': book, 'form': form}

    return render(request, 'books/update_book.html', context)


@login_required
def add_member(request):
    members = Member.objects.all()

    if request.method == 'POST':
        form = MemberForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('book')

    else:
        form = MemberForm()
    context = {'members': members, 'form': form}

    return render(request, 'members/add_member.html', context)



