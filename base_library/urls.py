from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name="home"),
    path('book', views.book_index, name="book"),
    path('add_book', views.add_book, name="add-book"),
    path('update_book', views.update_book, name="update-book"),
    path('add_member', views.add_member, name="add-member"),
    path('update_member', views.update_member, name="update-member"),
]