from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('book', views.book_index, name="book"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),

]