# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from json import dumps
import json
import datetime
from django.db import connection
# dictfetchall return  rows of sql as list of object dict
def myconverter(o):
    if isinstance(o, datetime.date):
        return o.__str__()
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
#get query from database  as list of object 
def executeQuery(query,returning=True):
    #define cursor
    cursor=connection.cursor()
    #execute query
    cursor.execute(query)
    # geting data  
    if returning:
        data = dictfetchall(cursor) 
        cursor.close() 
        return data
    # closing cusor
    cursor.close() 
#get id_priv from database
def getPriv(request):
    return executeQuery('select id_pri from user_privi where id_user= %d'%(request.user.id))[0].get('id_pri')
#check if user as admin
def isAdmin(request):
    return getPriv(request)==1
#check if user is operator
def isOperator(request):
    return getPriv(request)==2
#check if a user is user
def isUser(request):
    return getPriv(request)==3
# fetching privivelegs of users and redirect to path
def userToPath(request):
    if isAdmin(request) :
        return HttpResponseRedirect('/administrator')
    elif isOperator(request) :
        return HttpResponseRedirect('/operator')
    elif isUser(request):
        return HttpResponseRedirect('/users')
    else :
        return HttpResponse('ohooooooooooooooooo !!')

# app home page
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        if not request.user.is_authenticated():
            return render(request, 'index.html')
        return userToPath(request)
# view of login
class loginin(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'login.html')
    def post(self, request, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return userToPath(request)
        return render(request,'login.html',{'errors':"incorrect username or password"})
# view of logout page
class logoutin(TemplateView):
    def get(self, request, **kwargs):
        logout(request)
        return HttpResponseRedirect('/?next='+request.path)
# get info of users
class getInfo(TemplateView):
    def get(self, request, **kwargs):
         return HttpResponse('{"username":"'+ request.user.username +'","email":"'+ request.user.email+'"}')
# get info of users
class getStatique(TemplateView):
    def get(self, request, **kwargs):
        id=request.GET.get('id',False)
        if request.user.is_authenticated() and id:
            sql='select * from statique where id_sensor='+id
            return HttpResponse(dumps(executeQuery(sql),default=myconverter))
        return HttpResponse('ok')


