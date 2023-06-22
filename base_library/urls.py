from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name="home"),
    path('book', views.book_index, name="book"),
    path('add_book', views.add_book, name="add-book"),
    path('update_book/<int:pk>/', views.update_book, name="update-book"),
    path('add_member', views.add_member, name="add-member"),
    path('update_member/<int:pk>/', views.update_member, name="update-member"),
    path('member_index/', views.member_index, name="member_index"),
    path('member_detail/<int:member_id>/', views.member_detail, name="member_detail"),
    path('issue-book/', views.issue_book, name='issue_book'),
    path('issued-books/', views.issued_books, name='issued_books'),
]