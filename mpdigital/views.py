from django.shortcuts import render


def index(request):
    return render(request, "mpdigital/index.html")


def services(request):
    return render(request, "mpdigital/services.html")