from django.http import JsonResponse
from django.shortcuts import render
from municipalManagementUI import models
from patrolManagementUI import models as model2
import datetime


# Create your views here.
def patrolManagementUI(request):
    employee_id = request.COOKIES.get('employee_id')
    user = models.职工.objects.get(工号=employee_id)
    user_dict = {
        'name': user.姓名,
        'employee_id': user.工号,
        'position': '市政道路管理' if user.职能 == '1' else '道路巡查养护'
    }
    return render(request, 'patrolManagement.html', context=user_dict)


def patrolMap(request):
    today = datetime.date.today()
    Tasks = model2.日常巡查.objects.filter(巡查日期=today, 巡查状态='未巡查')
    return render(request, 'patrolMap.html', {'Tasks': Tasks})


# 返回所有道路对应的基本信息


def getRoadsLatlng(request):
    roadsLatlng = {}
    # 在道路基本档案中取出日常巡查表今日巡查任务的道路编号对应的档案
    today = datetime.date.today()
    TodayTasks = model2.日常巡查.objects.filter(巡查日期=today, 巡查状态='未巡查')
    for ToadyTask in TodayTasks:
        Roads = models.道路基本档案.objects.filter(道路编号=ToadyTask.巡查道路.道路编号)
    for singleRoad in Roads:
        roadsLatlng[singleRoad.道路编号] = singleRoad.getLatlng()
    return JsonResponse(roadsLatlng, safe=False)
