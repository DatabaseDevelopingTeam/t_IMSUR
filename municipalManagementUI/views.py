from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from login import models


def municipalManagementUI(request):
    id = request.COOKIES.get('employee_id')
    user = models.职工.objects.get(工号=id)
    user_dict = {
        'id': user.工号,
    }
    return render(request, 'municipalManagement.html')
