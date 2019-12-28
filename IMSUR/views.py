from django.http import request
from django.shortcuts import render


def page_not_found(request,exception):
    return render(request,'HandleException/404.html')


def page_error(request):
    return render(request,'HandleException/500.html')