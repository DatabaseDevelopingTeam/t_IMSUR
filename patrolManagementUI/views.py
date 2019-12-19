from django.shortcuts import render


# Create your views here.
def patrolManagementUI(request):
    return render(request,'patrolManagement.html')