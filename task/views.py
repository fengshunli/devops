# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, "task/index.html")


def once(request):
    return render(request, "task/once.html")


def inadd(request):
    return render(request, "task/add.html")


def history(request):
    return render(request, "task/history.html")
