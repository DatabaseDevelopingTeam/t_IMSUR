from django.urls import path, include
from . import views

app_name = 'patrolManagementUI'
urlpatterns = [
    path('', views.patrolManagementUI),
    path('patrolManagementUI/',views.patrolManagement),
]
