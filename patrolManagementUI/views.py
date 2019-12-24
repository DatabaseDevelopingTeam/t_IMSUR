from django.shortcuts import render
from municipalManagementUI import models

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
    return render(request,'patrolMap.html')