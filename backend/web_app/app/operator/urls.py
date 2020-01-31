from django.conf.urls import url, include
from app.operator import views

#url partterns of operator
urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^setProfile/', views.setProfile.as_view()),
    url(r'^createUser/', views.createUser.as_view()),
    url(r'^deleteUser/', views.deleteUser.as_view()),
    url(r'^updateUser/', views.updateUser.as_view()),
    url(r'^getInfo/', views.getInfo.as_view()),
    url(r'^getListUsers/', views.getListUser.as_view()),
    url(r'^getListSensor/', views.getListSensor.as_view()),
     url(r'^getInfoSensor/', views.getInfoSensor.as_view()),
    url(r'^getListSensorOf/',views.getListSensorOf.as_view()),
    url(r'^getInfoSensor/', views.getInfoSensor.as_view()),
    url(r'^',views.HomePageView.as_view()),
]
