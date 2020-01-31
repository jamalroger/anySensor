from django.conf.urls import url 
from app.users import views

#url partterns of site tourism
urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^setProfile/', views.setProfile.as_view()),
    url(r'^getInfo/', views.getInfo.as_view()),
    url(r'^createSensor/', views.createSensor.as_view()),
    url(r'^deleteSensor/', views.deleteSensor.as_view()),
    url(r'^getListSensor/', views.getListSensor.as_view()),
    url(r'^getInfoSensor/', views.getInfoSensor.as_view()),
    url(r'^setSensor/', views.setSensor.as_view()),
    url(r'^', views.HomePageView.as_view()),
]
