from django.shortcuts import render, redirect
from django.http import response, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from municipalManagementUI import models
from patrolManagementUI import models as pmodels
import datetime


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
    roadType = request.POST.get('roadType')
    # 建立道路基本档案
    road = models.道路基本档案(道路名称=roadName,
                         道路等级=models.道路等级.objects.get(道路等级=roadLevel),
                         道路编号=roadId,
                         经度=float(lng), 纬度=float(lat))

    road.save()
    # 保存一对一的车行道信息
    路面类型 = models.路面类型.objects.get(路面类型=roadType)
    models.车行道(道路编号=road, 路面类型=路面类型).save()
    # 建立今日巡查任务
    pmodels.日常巡查任务(巡查日期=datetime.date.today(),
                   巡查道路=road, 巡查状态=1).save()
    pmodels.定期巡查任务(巡查日期=datetime.date.today(),
                   巡查道路=road, 巡查状态=1).save()
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


'''技术指标计算'''


#######################################
###############计算RQI ################
#######################################


def countingRQI(IRI):
    RQI = 4.98 - 0.34 * IRI
    return RQI if RQI >= 0 else 0


# 根据RQI和道路等级给出路面行驶质量等级
def getLevelByRQI(RQI, roadLevel):
    # (roadLevel,(RQIRange,level))
    evaluationCriteria = {
        '1': {
            (4.10, 4.98): 'A',
            (3.6, 4.1): 'B',
            (2.5, 3.6): 'C',
            (0, 2.5): 'D',
        },
        '2': {
            (3.6, 4.98): 'A',
            (3.0, 3.6): 'B',
            (2.4, 3.0): 'C',
            (0, 2.4): 'D',
        },
        '3': {
            (3.4, 4.98): 'A',
            (2.8, 3.4): 'B',
            (2.2, 2.8): 'C',
            (0, 2.2): 'D',
        },
    }

    key = findIndexRangeByIndex(RQI, evaluationCriteria[roadLevel])
    return evaluationCriteria[roadLevel][key]


def inRange(Index, rangeTuple):
    if rangeTuple[0] <= Index <= rangeTuple[1]:
        return True
    return False


def findIndexRangeByIndex(Index, dic):
    for key in dic.keys:
        if inRange(Index, key):
            return key
    return 0, 0


####################################
#############计算PCI################
####################################


损坏类型表 = {
    '沥青路面': {
        '裂缝类': ['线裂', '网裂', '龟裂'],
        '变形类': ['拥包', '车辙', '沉陷', '翻浆'],
        '松散类': ['剥落', '坑槽', '啃边'],
        '其他类': ['路框差', '唧浆', '泛油'],
    },
    '混凝土路面': {
        '裂缝类': ['线裂', '板角断裂', '边角裂缝', '交叉裂缝和破碎板'],
        '接缝破坏类': ['接缝料损坏', '边角剥落'],
        '表面破坏类': ['坑洞', '表面纹裂', '层状剥落'],
        '其他类': ['错台', '拱胀', '唧浆', '路框差', '沉陷'],
    },
}


# 根据PCI和道路等级给出路面损坏状况等级
def getLevelByPCI(PCI, roadLevel):
    # (roadLevel,(PCIRange,level))
    evaluationCriteria = {
        '1': {
            (90, 100): 'A',
            (75, 90): 'B',
            (65, 75): 'C',
            (0, 65): 'D',
        },
        '2': {
            (85, 100): 'A',
            (70, 85): 'B',
            (60, 70): 'C',
            (0, 60): 'D',
        },
        '3': {
            (80, 100): 'A',
            (65, 80): 'B',
            (60, 65): 'C',
            (0, 60): 'D',
        },
    }

    key = findIndexRangeByIndex(PCI, evaluationCriteria[roadLevel])
    return evaluationCriteria[roadLevel][key]


# 为单条道路计算PCI
def countingPCIForOneRoad(regularDamageRecords):
    PCI_sum = 0
    for singleDamageRecord in regularDamageRecords:
        # 损坏类型
        damageType = singleDamageRecord.损坏类型
        # 损坏密度 = 损坏面积/检查面积
        damageArea = countingDamageArea(damageType.损坏面积计算方法代号, singleDamageRecord.损坏长,
                                        singleDamageRecord.损坏宽,
                                        singleDamageRecord.损坏高)
        detectionArea = singleDamageRecord.检查总长 * singleDamageRecord.检查总宽
        damageDensity = damageArea / detectionArea
        PCI_sum += countingSinglePCIForOneRecord(damageType, damageDensity)
    PCI_average = PCI_sum / len(regularDamageRecords)
    return 100 - PCI_average


# 计算损坏面积
def countingDamageArea(computingMethodCode, L, W, H):  # 长，宽，高
    computingDict = {
        '1': L * W,
        '2': L,
        '3': 4,
        '4': L * 0.2
    }
    if computingMethodCode in computingDict.keys():
        return computingDict[computingMethodCode]
    return 0


'''
 n——单类损坏类型数
 对沥青路面，n取值为4，分别对应裂缝类、变形类、松散类和其他类；
 对混凝土路面，n取值为4，分别对应裂缝类、接缝破坏类、表面破坏类和其他类；
 m——某单类损坏所包含的单项损坏类型数
'''


# 为单条道路的单次损坏记录计算PCI被减项
def countingSinglePCIForOneRecord(损坏类型obj, 损坏密度):
    return countingDP(损坏类型obj, 损坏密度) * countingWij(损坏类型obj, 损坏密度)


# 获取某种路面的某种损坏类型的对应损坏密度的扣分分值
# get DPij
def countingDP(损坏类型obj, 损坏密度):
    if models.路面损坏单项扣分表.objects.filter(损坏类型=损坏类型obj, 损坏密度_gte=损坏密度).exsits():
        return models.路面损坏单项扣分表.objects.filter(损坏类型=损坏类型obj, 损坏密度_gte=损坏密度)[0].扣分分值
    return 1


# counting Uij
def countingUij(损坏类型obj, 损坏密度):
    路面类型 = 损坏类型obj.要引用的路面类型.路面类型
    singleRoadTypeDict = 损坏类型表[路面类型]
    key = ''
    for k, v in singleRoadTypeDict:
        if 损坏类型obj.损坏类型 in v:
            key = k

    singlePoint = models.路面损坏单项扣分表.objects.get(损坏类型=损坏类型obj, 损坏密度=损坏密度).扣分分值
    sumPoint = 0
    for singleDamageType in singleRoadTypeDict[key]:
        损坏类型 = models.路面损坏类型.objects.get(要引用的路面类型=models.路面类型.objects.get(路面类型=路面类型), 损坏类型=singleDamageType)
        sumPoint += models.路面损坏单项扣分表.objects.get(损坏类型=损坏类型, 损坏密度=损坏密度).扣分分值
    return singlePoint / sumPoint


# counting Wij
def countingWij(损坏类型obj, 损坏密度):
    Uij = countingUij(损坏类型obj, 损坏密度)
    return 3 * (Uij ** 3) - 5.5 * (Uij ** 2) + 3.5 * Uij


####################################
#############计算PQI################
####################################
# 根据PCI和道路等级给出路面损坏状况等级


def getLevelByPQI(PQI, roadLevel):
    # (roadLevel,(PQIRange,level))
    evaluationCriteria = {
        '1': {
            (90, 100): 'A',
            (75, 90): 'B',
            (65, 75): 'C',
            (0, 65): 'D',
        },
        '2': {
            (85, 100): 'A',
            (70, 85): 'B',
            (60, 70): 'C',
            (0, 60): 'D',
        },
        '3': {
            (80, 100): 'A',
            (65, 80): 'B',
            (60, 65): 'C',
            (0, 60): 'D',
        },
    }

    key = findIndexRangeByIndex(PQI, evaluationCriteria[roadLevel])
    return evaluationCriteria[roadLevel][key]


def countingPQI(RQI, PCI, roadLevel):
    # T——RQI分值转换系数，T取值为20T——RQI分值转换系数，T取值为20
    T = 20
    weightDict = {
        'RQI': {
            '1': 0.6,
            '2': 0.6,
            '3': 0.4,
        },
        'PCI': {
            '1': 0.4,
            '2': 0.4,
            '3': 0.6,
        }
    }
    return T * RQI * weightDict['RQI'][roadLevel] + PCI * weightDict['RQI'][roadLevel]


# 返回评估页面
def evaluation(request):
    roads = models.道路基本档案.objects.all()
    return render(request, 'evaluation.html', context={'roads': roads})


# 生成评估数据
@csrf_exempt
def evaluate(request):
    roadId = request.POST.get('roadId')
    year = request.POST.get('year')
    road = models.道路基本档案.objects.get(道路编号=roadId)
    # 计算路面行驶质量评价
    if pmodels.定期检测记录.objects.filter(道路编号=road, 巡查日期__year=year).exists():
        # 某道路某年的所有定期巡查记录
        regularDetectionRecords = pmodels.定期检测记录.objects.filter(道路编号=road, 巡查日期__year=year)

        IRI_of_sum = 0
        PCI_of_sum = 0
        # 取出数据
        for i in range(len(regularDetectionRecords)):
            singleRecord = regularDetectionRecords[i]
            # 取出对应的平整度记录
            IRI = pmodels.路面平整度检测记录.objects.get(定期检查记录编号=singleRecord).IRI
            IRI_of_sum += IRI
            # 取出对应的定期检查损坏记录并计算单次巡查的PCI
            regularDamageRecords = pmodels.路面定期检查损害记录.objects.filter(定期检查记录编号=singleRecord)
            PCI_of_sum += countingPCIForOneRoad(regularDamageRecords)

        # 计算RQI
        IRI_average = IRI_of_sum / len(regularDetectionRecords)
        RQI_average = countingRQI(IRI_average)
        RQI_level = getLevelByRQI(RQI_average, road.道路等级)
        # 计算PCI
        PCI_average = PCI_of_sum / len(regularDetectionRecords)
        PCI_level = getLevelByPCI(RQI_average, road.道路等级)
        # 计算PQI
        PQI_average = countingPQI(RQI_average, PCI_average, road.道路等级)
        PQI_level = getLevelByPQI(PQI_average, road.道路等级)
        # 评价记录写入数据库
        evaluateRecord = models.道路技术状况评价年报表(道路编号=road,
                                            评价日期=datetime.date.today(),
                                            RQI=RQI_average,
                                            RQI等级=RQI_level,
                                            PCI=PCI_average,
                                            PCI等级=PCI_level,
                                            PQI=PQI_average,
                                            PQI等级=PQI_level)
        evaluateRecord.save()
        evaluateRecordDict = {
            'road': str(road),
            'year': year,
            'RQI': PQI_average,
            'RQILevel': PQI_level,
            'PCI': PCI_average,
            'PCILevel': PCI_level,
            'PQI': PQI_average,
            'PQILevel': PQI_level,
        }
        return JsonResponse(evaluateRecordDict,safe=False)
    else:
        return HttpResponse("-1")  # 无记录！


# 通过道路编号获取其已有的检测记录的年份
def getYearByRoadId(request):
    roadId = request.GET.get('roadId')
    road = models.道路基本档案.objects.get(道路编号=roadId)
    if pmodels.定期检测记录.objects.filter(道路编号=road).exists():
        regularDetectionRecords = pmodels.定期检测记录.objects.filter(道路编号=road)
        years = []
        for i in range(len(regularDetectionRecords)):
            record = regularDetectionRecords[i]
            year = record.yearOfDate()
            if year not in years:
                years.append(year)
        return JsonResponse(years, safe=False)
    else:
        return JsonResponse(['没有查询到数据'], safe=False)
