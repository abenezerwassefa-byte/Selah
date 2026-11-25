from django.shortcuts import render


def auth_page(request):
    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')
