from django.shortcuts import render

# Create your views here.


def control(request):
    return render(request, 'control.html')


def monitor(request):
    return render(request, 'monitor.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')
