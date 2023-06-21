from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name="home"),
    path('book', views.book_index, name="book"),
    path('add_book', views.add_book, name="add-book"),
    path('add_member', views.add_member, name="add-member"),
    # path('login', views.login_user, name="login"),
    # path('register', views.register, name="register"),
    # path('logout', views.logout_user, name="logout"),

]