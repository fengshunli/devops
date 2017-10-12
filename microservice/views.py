import requests
from django.http import JsonResponse
from django.shortcuts import render

from microservice.models import TbEurekaManager


def index(request):
    return render(request, "microservice/index.html")


def add(request):
    """
    添加一个EUREKA服务，通过该服务找到注册的其他微服务，实现发现服务进行监控功能
    :param request:
    :return:
    """
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


def delete(request):
    """
    删除一个EUREKA服务，同时删除原有的监控数据
    :param request:
    :return:
    """
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