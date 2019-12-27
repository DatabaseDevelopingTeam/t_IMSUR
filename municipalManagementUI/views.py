from django.shortcuts import render
from django.http import response, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from municipalManagementUI import models


def municipalManagementUI(request):
    employee_id = request.COOKIES.get('employee_id')
    user = models.职工.objects.get(工号=employee_id)
    user_dict = {
        'name': user.姓名,
        'employee_id': user.工号,
        'position': '市政道路管理' if user.职能 == '1' else '道路巡查养护',
    }
    return render(request, 'municipalManagement.html', context=user_dict)


def roadManagement(request):
    return render(request, 'roadManagement.html', context={'roads': models.道路基本档案.objects.all()})


@csrf_exempt
def addRoadBasicInfo(request):
    # print(request.POST)
    roadId = request.POST.get('roadId')
    roadName = request.POST.get('roadName')
    roadLevel = request.POST.get('roadLevel')
    lat = request.POST.get('lat')
    lng = request.POST.get('lng')
    road = models.道路基本档案(道路名称=roadName,
                         道路等级=models.道路等级.objects.get(道路等级=roadLevel),
                         道路编号=roadId,
                         经度=float(lng), 纬度=float(lat))

    road.save()
    return HttpResponse('添加成功')
    # return HttpResponse('表单异常!', status=403)


@csrf_exempt
def checkIfRoadIdExists(request):
    roadId = request.POST.get('roadId')
    if models.道路基本档案.objects.filter(道路编号=roadId).exists():
        return HttpResponse('0')
    return HttpResponse('1')


@csrf_exempt
def getRoadInfoPopup(request):
    roadId = request.POST.get('roadId')
    dictRoad = models.道路基本档案.objects.get(道路编号=roadId).getDict()
    return render(request, 'roadInfoPopup.html', context=dictRoad)


@csrf_exempt
def getAllRoadsBasicInfo(request):
    roads = []
    for singleRoad in models.道路基本档案.objects.all():
        roads.append({'roadId': singleRoad.道路编号,
                      'roadName': singleRoad.道路名称,
                      'latlng': singleRoad.getLatlng(),
                      'roadLevel': singleRoad.道路等级.道路等级, })
    return JsonResponse(roads, safe=False)


def getRoadAddPopupContent(request):
    return render(request, 'roadAddPopupContent.html')


@csrf_exempt
def getRoadsLatlng(request):
    roadsLatlng = {}
    for singleRoad in models.道路基本档案.objects.all():
        roadsLatlng[singleRoad.道路编号] = singleRoad.getLatlng()
    return JsonResponse(roadsLatlng, safe=False)
