# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    return render(request, "asset/index.html")


def inadd(request):
    return render(request, "asset/add.html")


def add(request):
    return JsonResponse({"code": 100, "msg": "项目地址不能访问"}, safe=False)


def lists(request):
    return JsonResponse({"code": 100, "msg": "项目地址不能访问"}, safe=False)
