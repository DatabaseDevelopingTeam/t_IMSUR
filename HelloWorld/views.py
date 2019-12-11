from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    context = {'hellostr': 'Hello World'}
    return render(request, 'index.html', context)
