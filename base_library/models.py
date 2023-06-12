from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    quantity = models.IntegerField()
    shelf_location = models.TextField()
    availability = models.BooleanField(null=True, blank=True)


class Member(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    membership_ID = models.IntegerField()
    borrowed_books = models.IntegerField()
    penalty_status = models.BooleanField()


class Transaction(models.Model):
    book = models.ForeignKey(Book, related_name='books', on_delete=models.CASCADE, null=True)
    member = models.ForeignKey(Member, related_name='members', on_delete=models.CASCADE, null=True)
    issue_date = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(auto_now=True)
    return_date = models.DateTimeField(auto_now=True)
    rent_fee = models.DecimalField(max_digits=6, decimal_places=2)


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class Librarian(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    staff_ID = models.IntegerField()
    permission_role = models.BooleanField(default=0)
    shift_schedule = models.DateTimeField(auto_now=True)
# Create your models here.
