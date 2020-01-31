# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from json import dumps
import datetime
from app.views import executeQuery,isUser,userToPath
def myconverter(o):
    if isinstance(o, datetime.date):
        return o.__str__()
# check user if is authentified or not and request to his path
def check_user(request):
    if not request.user.is_authenticated():
            return HttpResponseRedirect('/')
    if not isUser(request):
            return userToPath(request)
# app home page
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        if check_user(request):
            return check_user(request)
        return render(request, 'users/index.html')
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
class createSensor(TemplateView):
    def get(self,request,**kwargs):
        if check_user(request):
            return check_user(request)
        id_user= request.user.id
        sensor_name = request.GET.get('sensor_name')
        model= request.GET.get('model')
        poids = request.GET.get('poids')
        date_fab = request.GET.get('date_fab')
        date_exp = request.GET.get('date_exp')
        des=request.GET.get('des')
        sql="insert into sensor(id_user,model,poids,date_fab,date_exp,des,sensor_name) values(%d,'%s',%d,'%s','%s','%s','%s')"%(int(id_user),model,int(poids),date_fab,date_exp,des,sensor_name)
        executeQuery(sql,False)
            # try:
            #     executeQuery(sql)
            #     return HttpResponse('ok')
            # except:
            #     return HttpResponse('ko')
        return JsonResponse({'is':True})
class deleteSensor(TemplateView):
    def get(self,request,**kwargs):
        id=request.GET.get('id',False)
        if id:
            sql='delete from sensor where id='+id
            executeQuery("SET FOREIGN_KEY_CHECKS = 0",False)
            executeQuery(sql,False)
            return HttpResponse('ok')
        return HttpResponse('ko')
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
class getListSensor(TemplateView):
    def get(self, request, **kwargs):
        if check_user(request):
            return check_user(request)
        sql='select * from sensor where id_user = %d'%(int(request.user.id))
        return HttpResponse(dumps(executeQuery(sql),default=myconverter),content_type='application/json; charset=utf-8')
class getInfoSensor(TemplateView):
    def get(self, request, **kwargs):
        if check_user(request):
            return check_user(request)
        id=request.GET.get('id',False)
        if id:
            sql="select * from sensor where id=%d and id_user=%d limit 1"%(int(id),int(request.user.id))
            res=executeQuery(sql)
            if not res:
                return HttpResponse("<h1>this Sensor is not for you</h1>")
            sql='select * from sensor,statique where sensor.id=statique.id_sensor and sensor.id=%d'%(int(id))
            if executeQuery(sql):
                d=executeQuery(sql)
            else:
                d=executeQuery('select * from sensor where id='+id)
            info = d[0]
            data=dumps(d,default=myconverter)
            return render(request, 'InfoSensor.html',{'data':data,'info':info})
        return  HttpResponse('kooooooooooooooooo')
class setSensor(TemplateView):
    def get(self, request, **kwargs):
        id = request.GET.get('id',False)
        val = request.GET.get('val',False)
        if id and val:
            sql='insert into statique values(%d,%d,\'%s\')'%(int(id),float(val),str(datetime.datetime.now()))
            executeQuery(sql,False)
            return  HttpResponse('ok')
        return  HttpResponse('ko')
