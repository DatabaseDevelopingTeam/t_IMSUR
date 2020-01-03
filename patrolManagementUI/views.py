import json

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
    Tasks = model2.日常巡查任务.objects.filter(巡查日期=today,巡查状态='1')
    return render(request, 'patrolMap.html', {"Tasks": Tasks})


# 返回所有道路对应的基本信息
@csrf_exempt
def getTodayRoadsBasicInfo(request):
    roads = []
    today = datetime.date.today()
    TodayTasks = model2.日常巡查任务.objects.filter(巡查日期=today, 巡查状态='1')
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
    # 在道路基本档案中取出日常巡查任务表今日巡查任务的道路编号对应的档案
    today = datetime.date.today()
    TodayTasks = model2.日常巡查任务.objects.filter(巡查日期=today, 巡查状态='1')
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
    employee_id=request.COOKIES.get('employee_id')
    user = models.职工.objects.get(工号=employee_id)
    Info['employeeId']=user.工号
    Info['employeeName']=user.姓名
    CarRoad=models.车行道.objects.get(道路编号=roadId)
    Roadtype=models.路面类型.objects.get(路面类型=CarRoad.路面类型.路面类型)
    DamageTypes=Roadtype.rn路面类型.all()
    i=1;
    for DamageType in DamageTypes:
        Info['%s'%(i)]=DamageType.损坏类型
        i=i+1
    Info['roadId']=Road.道路编号
    Info['roadName']=Road.道路名称
    Info['roadType']=CarRoad.路面类型.路面类型
    Info['length']='%s' % (i)
    return JsonResponse(Info,safe=False)


@csrf_exempt
def AddDailyPatrolRecord(request):
    employeeId=request.COOKIES.get('employee_id')
    user=models.职工.objects.get(工号=employeeId)
    roadId=request.POST.get('roadId')
    print('roadId:'+str(roadId))
    road=models.道路基本档案.objects.get(道路编号=roadId)
    time=datetime.date.today()
    #建立日常巡查记录档案
    DailyPatrolRecord=model2.日常巡查记录(巡查人员=user,道路编号=road,巡查日期=time)
    DailyPatrolRecord.save()
    roadType=request.POST.get('roadType')
    #获取路面类型表的对象
    roadTypeObject=models.路面类型.objects.get(路面类型=roadType)
    #建立日常巡查损坏记录档案
    # infos = request.POST.get('infos')
    infos=json.loads(request.POST.get('infos'))
    for v in infos.values():
        damageType=v['damageType']
        damageDetail=v['damageDetail']
        note=v['note']
        damageTypeObject=models.路面损坏类型.objects.get(要引用的路面类型=roadTypeObject,损坏类型=damageType)
        DailyPatrolDamageRecordObject=model2.日常巡查损害记录(日常巡查记录编号=DailyPatrolRecord,损坏类型=
                                                      damageTypeObject,损坏位置及情况描述=damageDetail,备注=note)
        DailyPatrolDamageRecordObject.save()
    DailyTask=model2.日常巡查任务.objects.get(巡查日期=time,巡查道路=road,巡查状态='1')
    DailyTask.巡查状态='2'
    DailyTask.save()
    Location=road.getLatlng()
    return JsonResponse(Location,safe=False)