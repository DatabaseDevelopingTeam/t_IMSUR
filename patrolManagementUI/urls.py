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

    path('patrolMap2/',views.patrolMap2),
    path('patrolMap2/getRoadsLatlng2/',views.getRoadsLatlng2),
    path('patrolMap2/getTodayRoadsBasicInfo2/',views.getTodayRoadsBasicInfo2),
    path('patrolMap2/getRoadInfoPopup2/',views.getRoadInfoPopup),
    path('patrolMap2/setupModalView2/',views.setupModalView2),
    path('patrolMap2/AddDailyPatrolRecord2/',views.AddDailyPatrolRecord2),
]
