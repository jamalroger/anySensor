# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from json import dumps
import django.middleware.csrf
import datetime
from app.views import executeQuery, isAdmin ,userToPath
def myconverter(o):
    if isinstance(o, datetime.date):
        return o.__str__()
# check user if is authentified or not and request to his path
def check_user(request):
    if not request.user.is_authenticated():
            return HttpResponseRedirect('/')
    if not isAdmin(request):
            return userToPath(request)
# app home page
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        if check_user(request) :
            return check_user(request)
        return render(request,'administrator/index.html')
# set profile user
class setProfile(TemplateView):
    def get(self, request, **kwargs):
        if check_user(request):
           return check_user(request)
        first_name=request.GET['first_name']
        last_name=request.GET['last_name']
        email=request.GET['email']
        cin=request.GET['cin']
        dn=request.GET['dn']
        city=request.GET['city']
        job=request.GET['job']
        tel=request.GET['tel']
        adresse=request.GET['adresse']
        user=User.objects.get(pk=request.user.id)
        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        user.save()
        sql="update info_user set cin='%s',dn='%s',city='%s',job='%s',tel='%s',adresse='%s' where id_user=%d"%(
            cin,dn,city,job,tel,adresse,request.user.id
        )
        if executeQuery(sql,False):
            return HttpResponse('ok ')
        return HttpResponse('ko')

class createUser(TemplateView):
    def get(self, request, **kwargs):
        if check_user(request):
            return check_user(request)
        username=request.GET['username']
        password=request.GET['password']
        first_name=request.GET['first_name']
        last_name=request.GET['last_name']
        email=request.GET['email']
        cin=request.GET['cin']
        dn=request.GET['dn']
        city=request.GET['city']
        job=request.GET['job']
        tel=request.GET['tel']
        adress=request.GET['adresse']
        user=User.objects.create_user(username,email,password)
        user.first_name=first_name
        user.last_name=last_name
        executeQuery('insert into user_created_by values(%d,%d)'%(request.user.id,user.id),False)
        executeQuery('insert into user_privi values(%d,2)'%(user.id),False)
        executeQuery("insert into user_info values(%d,'%s','%s','%s','%s','%s','%s')"%(user.id,cin,dn,job,city,tel,adress),False)
        user.save()
        return HttpResponse('ohoooooooooooooooooooooooooo!!!!')
class updateUser(TemplateView):
    def get(self, request, **kwargs):
        if request.user.is_authenticated():
           return render(request, 'main.html')
        return HttpResponse('ohoooooooooooooooooooooooooo!!!!')
class deleteUser(TemplateView):
    def get(self, request, **kwargs):
        if check_user(request):
            return check_user(request)
        id=request.GET.get('id',False)
        if id :
            executeQuery("SET FOREIGN_KEY_CHECKS = 0",False)
            user=User.objects.get(pk=id)
            user.delete()
            return HttpResponse("ok")
        return HttpResponse("ko")
class getInfo(TemplateView):
    def get(self, request, **kwargs):
        if check_user(request):
            return check_user(request)
        id=request.GET.get('id',False)
        if not id :
            sql='select id,first_name,last_name,email,job,cin,dn,city,adresse,tel from auth_user,user_info where auth_user.id=user_info.id_user and auth_user.id=%d'%(request.user.id)
        else :
            sql='select id,first_name,last_name,email,job,cin,dn,city,adresse,tel from auth_user,user_info where auth_user.id=user_info.id_user and auth_user.id=%d'%(int(id))
        response=HttpResponse(dumps(executeQuery(sql),default=myconverter),content_type='application/json; charset=utf-8')
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
class getListUser(TemplateView):
    def get(self, request, **kwargs):
        if check_user(request):
            return check_user(request)
        sql='select id,first_name,last_name,email,username from auth_user,user_created_by where auth_user.id=user_created_by.id_sub and user_created_by.id_super=%d'%(request.user.id)
        return HttpResponse(dumps(executeQuery(sql),default=myconverter),content_type='application/json; charset=utf-8')
class getListUserOfUser(TemplateView):
    def get(self, request, **kwargs):
        if check_user(request):
            return check_user(request)
        sql='select id,username,first_name,last_name,email from auth_user,user_created_by where auth_user.id=user_created_by.id_sub and user_created_by.id_super=%d'%(int(request.GET['id']))
        return HttpResponse(dumps(executeQuery(sql),default=myconverter),content_type='application/json; charset=utf-8')
class getListSensor(TemplateView):
    def get(self, request, **kwargs):
        if check_user(request):
            return check_user(request)
        sql='select sensor.id,username,model,sensor_name from sensor,auth_user where auth_user.id=sensor.id_user'
        return HttpResponse(dumps(executeQuery(sql),default=myconverter),content_type='application/json; charset=utf-8')
class getInfoSensor(TemplateView):
    def get(self, request, **kwargs):
        if check_user(request):
            return check_user(request)
        id=request.GET.get('id',False)
        if id: 
            sql='select * from sensor,statique where sensor.id=statique.id_sensor  and sensor.id=%d'%(int(id))
            if executeQuery(sql):
                d = executeQuery(sql)
            else:
                d = executeQuery('select * from sensor where id='+id)
            info = d[0]
            data=dumps(d,default=myconverter)
            return render(request, 'InfoSensor.html',{'data':data,'info':info})
        return  HttpResponse('kooooooooooooooooo')
# get token csrf_token
class getToken(TemplateView):
    def get(self, request, **kwargs):
        response = HttpResponse('{"csrf":"' + django.middleware.csrf.get_token(request)+ '"}',content_type='application/json; charset=utf-8')
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response

