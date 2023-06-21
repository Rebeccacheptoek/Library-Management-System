from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm
from .models import CustomUser


# class register(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/register.html"

def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('home')

        else:
            return render(request, 'registration/register.html', {'form': form})

    else:
        form = CustomUserCreationForm()
        return render(request, 'registration/register.html', {'form': form})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        print(email, password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            form = AuthenticationForm()
            return render(request, 'registration/login.html', {'form': form})

    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'registration/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')