import logging
from xml.etree import ElementTree

import requests
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect

logger = logging.getLogger(__name__)


def index(request):
    applications_str = requests.get('http://eureka.didispace.com/eureka/apps').text

    root = ElementTree.fromstring(applications_str)
    list_application = root.getiterator("application")

    application_size = 0
    instance_size = 0
    for application in list_application:
        application_size = application_size + 1
        print('\t application:', application.find('name').text)
        instance_list = application.getiterator('instance')
        for instance in instance_list:
            instance_size = instance_size + 1
            print('\t |- instanceId', instance.find('instanceId').text)
            print('\t |- hostName', instance.find('hostName').text)
            print('\t |- app', instance.find('app').text)
            print('\t |- ipAddr', instance.find('ipAddr').text)
            print('\t |- status', instance.find('status').text)
            print('\t |- statusPageUrl', instance.find('statusPageUrl').text)
            print('\t |- healthCheckUrl', instance.find('healthCheckUrl').text)

    context = {
        "application_size": application_size,
        "instance_size": instance_size
    }
    return render(request, "index.html", context)


def login(request):
    if request.method == 'GET':
        return JsonResponse({"code": 403, "errmsg": "请求不允许"}, safe=False)
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            logger.info("+" * 100)
            logger.info(f"({username}) 登陆了")
            logger.info("+" * 100)
            return JsonResponse({"code": 200}, safe=False)
        else:
            logger.error("x" * 100)
            logger.error(f"({username}) 尝试登录，输入了错误的密码({password})")
            logger.error("x" * 100)
            return JsonResponse({"code": 403, "msg": "账号或密码错误"}, safe=False)


@login_required
def logout(request):
    logger.info("-" * 100)
    logger.info(f"({request.user.username}) 登出了")
    logger.info("-" * 100)
    auth.logout(request)
    return HttpResponseRedirect("login")


@login_required
def changepwd(request):
    if request.method == 'GET':
        form = ChangepwdForm()
        return render(request, 'chameleon/changepwd.html', {'form': form})
    else:
        form = ChangepwdForm(request.POST)
        if form.is_valid():
            username = request.user.username
            oldpassword = request.POST.get('oldpassword', '')
            user = auth.authenticate(username=username, password=oldpassword)
            if user is not None and user.is_active:
                newpassword = request.POST.get('newpassword1', '')
                if oldpassword == newpassword:
                    logger.error('x' * 100)
                    logger.error(f"({username}) 尝试修改密码，旧密码和新密码不能相同({oldpassword})({newpassword})")
                    logger.error('x' * 100)
                    return render(request, 'chameleon/changepwd.html', {'form': form, 'error_msg': "旧密码和新密码不能相同"})
                try:
                    validate_password(newpassword)
                except ValidationError as e:
                    return render(request, 'chameleon/changepwd.html', {'form': form, 'error_msg': e})
                logger.info('ok ' * 100)
                logger.info(f"({username}) 修改了密码，原密码({oldpassword}),新密码({newpassword})")
                logger.info('ok ' * 100)
                user.set_password(newpassword)
                user.save()
                return render(request, 'chameleon/index.html', {'changepwd_success': True})
            else:
                logger.error('x' * 100)
                logger.error(f"({username}) 尝试修改密码，输入了错误的密码({oldpassword})")
                logger.error('x' * 100)
                return render(request, 'chameleon/changepwd.html', {'form': form, 'error_msg': "原密码不正确"})
        else:
            return render(request, 'chameleon/changepwd.html', {'form': form})
