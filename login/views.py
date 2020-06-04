from django.shortcuts import render


def index(request):
    context = {
        'price1': 100
    }
    return render(request, 'login/index.html', context)
