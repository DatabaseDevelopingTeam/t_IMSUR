import random
import time

from django.http import HttpResponse
from django.shortcuts import render, redirect
from municipalManagementUI.models import 职工


def forwardToLogin(request):
    return redirect('/login')


def login(request):
    employee_id = request.COOKIES.get('employee_id')
    ticket = request.COOKIES.get('ticket')
    # cookies中有令牌信息(勾选了自动登录，且cookie还未失效)
    if ticket:
        user = 职工.objects.get(工号=employee_id)
        position = user.职能
        if user.ticket == request.COOKIES['ticket']:  # 校验令牌
            if position == '1':
                return redirect('/municipalManagement')
            else:
                return redirect('/patrolManagement')
        else:  # 令牌不一致
            return render(request, 'login.html')
    # cookies失效或者未设置自动登录
    else:
        return render(request, 'login.html')


def trueLogin(request):
    if request.method == 'POST':
        # 获取表单参数
        employee_id = request.POST.get('employee_id')
        password = request.POST.get('password')
        autoLogin = request.POST.get('autoLogin')
        print('employee_id:'+str(employee_id))
        # 查询用户是否在数据库中
        if 职工.objects.filter(工号=employee_id).exists():
            user = 职工.objects.get(工号=employee_id)
            position = user.职能
            if user.密码 == password:  # 密码正确
                # 为用户生成令牌
                ticket = generateTicket()
                # 生成响应对象
                if position == '1':
                    response = redirect('/municipalManagement')
                else:
                    response = redirect('/patrolManagement')

                response.set_cookie('employee_id', employee_id, max_age=60 * 60 * 8)  # 设置cookie生存期为8小时
                # 如果设置了'记住登录状态'
                if autoLogin:
                    # 绑定令牌到cookie里面，如果用户重新访问登录页面就做验证
                    response.set_cookie('ticket', ticket, max_age=60 * 60 * 8)
                    # 将令牌存到服务器
                    user.ticket = ticket
                    user.save()  # 保存用户数据库
                return response
            else:
                return HttpResponse('用户密码错误')
        else:
            return HttpResponse('用户不存在')
    pass


# 　随机生成令牌
def generateTicket():
    ticket = ''
    for i in range(15):
        s = 'abcdefghijklmnopqrstuvwxyz123456789'
        # 获取随机的字符串
        ticket += random.choice(s)
    now_time = int(time.time())
    ticket = 'TK' + ticket + str(now_time)
    return ticket
