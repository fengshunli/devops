# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, "task/index.html")


def once(request):
    return render(request, "task/once.html")


def inadd(request):
    return render(request, "task/add.html")


def inadd_shell(request):
    return render(request, "task/add_shell.html")


def history(request):
    return render(request, "task/history.html")


def details(request):
    return render(request, "task/details.html")
