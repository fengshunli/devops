from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, "microservice/index.html")


def add(request):
    target_brand_name = request.POST.get("target_brand_name", "")
    confirm_status = request.POST.get("confirm_status", "")
    match_status = request.POST.get("match_status", "")
    current_page = request.POST.get("current_page", 1)
    username = request.user.username
    records = service.list_brand(username, target_brand_name, confirm_status, match_status, current_page)
    return render(request, 'chameleon/match/brand_table.html', {"records": records})
    return render(request, "microservice/index.html")