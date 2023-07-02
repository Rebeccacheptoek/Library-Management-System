from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView

from base_library.forms import BookForm, MemberForm
from base_library.models import Book, Member, Transaction
from users.forms import CustomUserCreationForm


def dashboard(request):
    transactions = Transaction.objects.all()
    issued_books_count = transactions.filter(is_returned=False).count()
    returned_books_count = transactions.filter(is_returned=True).count()

    books = Book.objects.all()
    book_labels = [book.title for book in books]
    book_quantities = [book.quantity for book in books]

    members = Member.objects.all()
    member_names = [member.name for member in members]
    loan_amounts_list = [float(member.debt) for member in members]

    context = {
        'member_names': member_names,
        'loan_amounts_list': loan_amounts_list,
        'book_labels': book_labels,
        'book_quantities': book_quantities,
        'issued_books_count': issued_books_count,
        'returned_books_count': returned_books_count,
    }
    return render(request, 'books/book_report.html', context)


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def book_index(request):
    books = Book.objects.all()
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    else:
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


def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    context = {'book': book}
    return render(request, 'books/book_detail.html', context)


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

                return redirect('issue_book')
            else:
                error_message = 'Book is not available'
        else:
            error_message = 'Member has outstanding debt'

        return render(request, 'books/book_issue_error.html', {'error_message': error_message})

    issued_transactions = Transaction.objects.filter(is_returned=False)
    returned_books = Transaction.objects.filter(is_returned=True)

    context = {'members': members, 'books': books, 'issued_transactions': issued_transactions,
               'returned_books': returned_books}

    return render(request, 'books/book_issue.html', context)


def issued_books(request):
    issued_transactions = Transaction.objects.filter(is_returned=False)
    return render(request, 'books/issued_books.html', {'issued_transactions': issued_transactions})


def return_book(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)

    if request.method == 'POST':
        return_option = request.POST.get('return_option')

        if return_option == 'return':
            transaction.is_returned = True
            transaction.save()

            # Increment book quantity by 1
            book = transaction.book
            book.quantity += 1
            book.save()
    return redirect('issue_book')


def search_books(request):
    search_query = request.GET.get('search_query', '')
    books = Book.objects.filter(title__icontains=search_query) | Book.objects.filter(author__icontains=search_query)
    context = {'books': books, 'search_query': search_query}
    return render(request, 'search_results.html', context)


def delete(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'The book has been deleted successfully.')

        return redirect('book')
    return render(request, 'books/delete.html', {'obj': book})
