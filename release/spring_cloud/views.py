from django.shortcuts import render


def index(request):
    return render(request, "release/git-spring-mvn.html")
