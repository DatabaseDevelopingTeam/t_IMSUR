from django.urls import path, include
from . import views

app_name = 'municipalManagementUI'
urlpatterns = [
    path('',views.municipalManagementUI)
]