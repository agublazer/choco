from django.shortcuts import render


def index(request):
    context = {
        'price1': 100
    }
    return render(request, 'login/index.html', context)


def login(request):
    context = {
        'price1': 100
    }
    return render(request, 'login/login.html', context)


def register(request):
    context = {
        'price1': 100
    }
    return render(request, 'login/register.html', context)
