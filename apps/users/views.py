from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView
from django.contrib.auth import authenticate, login
# Create your views here.


def index(request):

    return render(request, 'sjxf/basetables.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                # 登录
                login(request, user)
                return render(request, 'base.html')
            else:
                return render(request, 'users/login.html', {'msg': '密码输入错误'})
        else:
            return render(request, 'users/login.html', {'msg': '用户不存在'})

    elif request.method == 'GET':
        return render(request, 'users/login.html')
