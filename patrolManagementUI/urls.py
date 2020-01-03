from django.urls import path, include
from . import views

app_name = 'patrolManagementUI'
urlpatterns = [
    path('', views.patrolManagementUI),
    path('patrolMap/',views.patrolMap),
    path('patrolMap/getRoadsLatlng/',views.getRoadsLatlng),
    path('patrolMap/getTodayRoadsBasicInfo/',views.getTodayRoadsBasicInfo),
    path('patrolMap/getRoadInfoPopup/',views.getRoadInfoPopup),
    path('patrolMap/setupModalView/',views.setupModalView),
    path('patrolMap/AddDailyPatrolRecord/',views.AddDailyPatrolRecord),
]
