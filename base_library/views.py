from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView

from base_library.forms import BookForm, MemberForm
from base_library.models import Book, Member, Transaction
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


def member_index(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'members/member_list.html', context)


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


@login_required
def update_member(request, pk):
    member = Member.objects.get(id=pk)
    form = MemberForm(instance=member)

    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('book')

    context = {'member': member, 'form': form}

    return render(request, 'members/update_member.html', context)


def member_detail(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    borrowed_books = Transaction.objects.filter(member=member, is_returned=False)
    penalty_status = member.penalty_status
    context = {'member': member, 'borrowed_books': borrowed_books, 'penalty_status': penalty_status}
    return render(request, 'members/member_detail.html', context)


def issue_book(request):
    members = Member.objects.all()
    books = Book.objects.filter(quantity__gt=0)

    if request.method == 'POST':
        member_id = request.POST.get('member')
        book_id = request.POST.get('book')

        member = get_object_or_404(Member, id=member_id)
        book = get_object_or_404(Book, id=book_id)

        if member.debt <= 500:
            rent_fee = 10.00
            if book.quantity > 0:
                # Reduce the quantity of the book
                book.quantity -= 1
                book.save()
                # Issue the book to the member
                transaction = Transaction.objects.create(member=member, book=book, is_returned=False, rent_fee=rent_fee)
                transaction.save()

                return redirect('book')
            else:
                error_message = 'Book is not available'
        else:
            error_message = 'Member has outstanding debt'

        return render(request, 'books/book_issue_error.html', {'error_message': error_message})

    return render(request, 'books/book_issue.html', {'members': members, 'books': books})


def issued_books(request):
    issued_transactions = Transaction.objects.filter(is_returned=False)
    return render(request, 'books/issued_books.html', {'issued_transactions': issued_transactions})


#  handles the HTTP request for returning a book
def return_book(request, member_id, book_id):
    transaction = get_object_or_404(Transaction, member_id=member_id, book_id=book_id)

    if transaction.return_date is None:
        transaction.return_book()

    return redirect('issued_books')