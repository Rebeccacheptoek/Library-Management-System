from django.urls import path

from . import views

urlpatterns = [
    path('', views.frontend_home, name="frontend")
]