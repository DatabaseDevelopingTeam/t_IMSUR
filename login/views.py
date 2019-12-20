import random
import time

from django.http import HttpResponse
from django.shortcuts import render
from login.models import 职工


def loginUI(request):
    employee_id = request.COOKIES.get('employee_id')
    if employee_id:  # cookies中有id信息(勾选了自动登录，且cookie还未失效)
        user = 职工.objects.get(工号=employee_id)
        if user.ticket == request.COOKIES['ticket']:  # 校验令牌
            return render(request, 'municipalManagement.html')
    # cookies失效或者未设置自动登录
    return render(request, 'loginUI.html')


def login(request):
    if request.method == 'POST':
        # 如果登录成功，绑定参数到cookie中，set_cookie
        employee_id = request.POST.get('employee_id')
        password = request.POST.get('password')
        # 查询用户是否在数据库中
        if 职工.objects.filter(工号=employee_id).exists():
            user = 职工.objects.get(工号=employee_id)
            if user.密码 == password:  # 密码正确
                ticket = ''
                for i in range(15):
                    s = 'abcdefghijklmnopqrstuvwxyz123456789'
                    # 获取随机的字符串
                    ticket += random.choice(s)
                now_time = int(time.time())
                ticket = 'TK' + ticket + str(now_time)
                # 绑定令牌到cookie里面
                response = render(request, 'municipalManagement.html')
                # max_age 存活时间(秒)
                response.set_cookie('ticket', ticket, max_age=10000)
                response.set_cookie('employee_id', employee_id, max_age=10000)
                # 存在服务端
                user.ticket = ticket
                user.save()  # 保存
                return response
            else:
                return HttpResponse('用户密码错误')
        else:
            return HttpResponse('用户不存在')
    pass
