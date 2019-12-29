from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

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
    # Tasks = model2.日常巡查.objects.filter(巡查日期=today)
    Tasks = model2.日常巡查.objects.filter(巡查日期=today,巡查状态='1')
    return render(request, 'patrolMap.html', {"Tasks": Tasks})


# 返回所有道路对应的基本信息
@csrf_exempt
def getTodayRoadsBasicInfo(request):
    roads = []
    today = datetime.date.today()
    TodayTasks = model2.日常巡查.objects.filter(巡查日期=today, 巡查状态='1')
    for TodayTask in TodayTasks:
        roads.append({'roadId': TodayTask.巡查道路.道路编号,
                      'roadName': TodayTask.巡查道路.道路名称,
                      'latlng': TodayTask.巡查道路.getLatlng(),
                      'roadLevel': TodayTask.巡查道路.道路等级.道路等级, })
    return JsonResponse(roads, safe=False)


# 获取今日巡查道路的位置信息
@csrf_exempt
def getRoadsLatlng(request):
    roadsLatlng = {}
    # 在道路基本档案中取出日常巡查表今日巡查任务的道路编号对应的档案
    today = datetime.date.today()
    TodayTasks = model2.日常巡查.objects.filter(巡查日期=today, 巡查状态='1')
    for ToadyTask in TodayTasks:
        roadsLatlng[ToadyTask.巡查道路.道路编号] = ToadyTask.巡查道路.getLatlng()
    return JsonResponse(roadsLatlng, safe=False)


# 获取道路信息框
@csrf_exempt
def getRoadInfoPopup(request):
    roadId = request.POST.get('roadId')
    #dictRoad = models.道路基本档案.objects.get(道路编号=roadId).getDict()
    dicRoad=models.道路基本档案.objects.get(道路编号=roadId)
    return render(request, 'RoadBasicInfoPopup.html', {'Road':dicRoad})

@csrf_exempt
def setupModalView(request):
    Info = {}
    roadId=request.POST.get('roadId')
    Road=models.道路基本档案.objects.get(道路编号=roadId)
    # CarRoad=Road
    # Roadtype=models.路面类型.objects.get(路面类型=CarRoad.路面类型.路面类型)
    # DamageType=Roadtype.rn路面类型.all()
    # print(DamageType)
    Info['roadId']=Road.道路编号
    Info['roadName']=Road.道路名称
    #Info['']=CarRoad.路面类型
    return JsonResponse(Info,safe=False)