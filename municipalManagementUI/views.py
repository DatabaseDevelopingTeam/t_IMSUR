from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def municipalManagementUI(request):
    return render(request, 'municipalManagement.html')
