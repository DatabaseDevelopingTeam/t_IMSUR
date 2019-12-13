from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    context = {'hellostr': 'Hello World'}
    return render(request, 'index.html', context)
