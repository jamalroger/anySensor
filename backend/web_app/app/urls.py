from django.conf.urls import url , include
from app import views
#url partterns of site tourism
urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^login/', views.loginin.as_view()),
    url(r'^logout/', views.logoutin.as_view()),
    url(r'^getInfo/', views.getInfo.as_view()),
    url(r'^getStatique/', views.getStatique.as_view()),
    url(r'^administrator/', include('app.administrator.urls') ),
    url(r'^operator/', include('app.operator.urls') ),
    url(r'^users/', include('app.users.urls') ),
   
    
]