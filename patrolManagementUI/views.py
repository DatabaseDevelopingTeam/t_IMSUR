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
    return render(request,'patrolManagement.html',context=user_dict)


def patrolManagement(request):
    today=datetime.date.today()
    Tasks=model2.日常巡查.objects.get(巡查日期=today)
    return render(request,'patrolMap.html')
