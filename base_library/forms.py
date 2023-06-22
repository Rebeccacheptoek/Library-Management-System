from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from base_library.models import Book, Member


# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'quantity', 'shelf_location', 'is_available']


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name',
                  'email',
                  'address',
                  'phone',
                  'membership_ID',
                  'borrowed_books',
                  'penalty_status',
                  ]
