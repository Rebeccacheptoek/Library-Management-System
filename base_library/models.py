from datetime import datetime, timedelta

from django.db import models
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    quantity = models.IntegerField()
    shelf_location = models.TextField()
    is_available = models.BooleanField(null=True, blank=True, default=1)
    rent_per_day = models.DecimalField(max_digits=6, decimal_places=2, default=5.00)

    def get_availability_display(self):
        if self.is_available:
            if self.quantity > 0:
                return f"Yes ({self.quantity} available)"
            else:
                return "Yes (0 available)"
        else:
            return "No"


class Member(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    membership_ID = models.IntegerField()
    borrowed_books = models.IntegerField(default=0)
    debt = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    penalty_status = models.BooleanField(default=False)

    def update_borrowed_books(self):
        self.borrowed_books = self.transaction_set.filter(is_returned=False).count()
        self.save()

    def update_penalty_status(self):
        current_date = timezone.now().date()
        overdue_transactions = self.transaction_set.filter(member=self, is_returned=False, due_date__lt=current_date)
        self.penalty_status = overdue_transactions.exists()
        self.save()

    def calculate_penalty_amount(self):
        current_date = timezone.now().date()
        overdue_transactions = self.transaction_set.filter(member=self, is_returned=False, due_date__lt=current_date)
        penalty_amount = sum((transaction.due_date - current_date).days * transaction.book.rent_fee for transaction in
                             overdue_transactions)
        return penalty_amount if penalty_amount > 0 else 0


class Transaction(models.Model):
    book = models.ForeignKey(Book, related_name='books', on_delete=models.CASCADE, null=True)
    member = models.ForeignKey(Member, related_name='transactions', on_delete=models.CASCADE, null=True)
    issue_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True)
    rent_fee = models.DecimalField(max_digits=6, decimal_places=2)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.member} - {self.book}"

    def save(self, *args, **kwargs):
        # Calculate the due date as 14 days excluding weekends
        issue_date = self.issue_date.date()
        due_date = issue_date + timedelta(days=14)
        days_to_add = 0
        while days_to_add < 14:
            due_date += timedelta(days=1)
            if due_date.weekday() < 5:  # Monday to Friday (0 to 4)
                days_to_add += 1
        self.due_date = datetime.combine(due_date, datetime.min.time())

        super().save(*args, **kwargs)

    def return_book(self):
        self.return_date = timezone.now()

        # Calculate the rent fee if the book is returned after the due date
        if self.return_date > self.due_date:
            days_overdue = (self.return_date.date() - self.due_date.date()).days

            self.rent_fee = days_overdue * self.book.rent_per_day

        self.save()


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
