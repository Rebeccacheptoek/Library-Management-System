from django.urls import path

from frontend import views

urlpatterns = [
    path('', views.frontend, name="frontend")
]