from django.urls import path, include
from . import views

app_name = 'municipalManagementUI'
urlpatterns = [
    path('', views.municipalManagementUI),
    path('roadManagement/', views.roadManagement),
    path('roadManagement/addRoadBasicInfo/', views.addRoadBasicInfo),
    path('roadManagement/checkIfRoadIdExists/', views.checkIfRoadIdExists),
    path('roadManagement/getRoadInfoPopup/', views.getRoadInfoPopup),
    path('roadManagement/getAllRoadsLatLng/', views.getAllRoadsLatLng),
    path('roadManagement/getRoadAddPopupContent/',views.getRoadAddPopupContent),
]
