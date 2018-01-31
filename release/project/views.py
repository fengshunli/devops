from django.shortcuts import render
from django.http import JsonResponse
from release.models import ProjectGroup, Project

"""
项目管理
"""


def index(request):
    return render(request, "release/project/index.html")


def add(request):
    project_groups = ProjectGroup.objects.values("id", "name").all()
    return render(request, "release/project/add.html", {"project_groups": project_groups})


def add_project(request):
    project_name = request.POST.get("project_name")
    leader = request.POST.get("leader")
    project_group = request.POST.get("project_group")
    project_type = request.POST.get("project_type")
    scm_url = request.POST.get("scm_url")
    scm_type = request.POST.get("scm_type")
    remark = request.POST.get("remark")
    Project.objects.create(name=project_name, leader=leader, project_group_id=project_group, project_type=project_type,
                           scm_type=scm_type, remark=remark, scm_url=scm_url)
    return JsonResponse({"code": 200, "msg": "添加成功"}, safe=False)
