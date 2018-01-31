from django.shortcuts import render

"""
项目管理
"""


def index(request):
    return render(request, "release/project/index.html")


def add(request):
    return render(request, "release/project/add.html")
