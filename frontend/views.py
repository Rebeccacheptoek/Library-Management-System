from django.shortcuts import render


# Create your views here.
def frontend_home(request):
    return render(request, 'frontend/frontend.html')
