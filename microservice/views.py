import requests
from django.http import JsonResponse
from django.shortcuts import render

from microservice.models import TbEurekaManager


def index(request):
    eurekas = list(TbEurekaManager.objects.all())
    context = {
        "records": eurekas,
    }
    return render(request, "microservice/index.html", context)


def add(request):
    project_name = request.POST.get("projectName")
    project_url = request.POST.get("projectURL")
    manager = request.POST.get("manager")
    email = request.POST.get("email")

    # 判断该链接是不是euraka链接
    eureka_url = project_url + "/eureka/apps"
    eureka_request = requests.get(eureka_url)
    if eureka_request.status_code == 200:
        print(eureka_request.headers)
        if eureka_request.text.startswith("<applications>") and eureka_request.headers:
            apps = list(TbEurekaManager.objects.filter(eureka_url=project_url).all())
            if apps and len(apps) == 0:
                TbEurekaManager.objects.create(app=project_name,
                                               eureka_url=project_url,
                                               manager=manager,
                                               email=email)
                return JsonResponse({"code": 200, "msg": "添加成功"}, safe=False)
            return JsonResponse({"code": 100, "msg": "该项目地址已经存在"}, safe=False)
    return JsonResponse({"code": 100, "msg": "项目地址不能访问"}, safe=False)


def project_list(request):
    eurekas = list(TbEurekaManager.objects.all())
    return JsonResponse({"code": 200, "data": eurekas}, safe=False)
