# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response,redirect

# Create your views here.

def login(request):
    if request.method == 'POST':
        user = request.POST.get('username',None)
        pwd = request.POST.get('password',None)
        if user == 'alex' and pwd == '123':
            request.session['is_login'] = {'user':user}
            return redirect('/web02/index/')
        else:
            return render_to_response('web02/login.html',{'msg':'用戶名或密碼錯誤。'})
    return render_to_response('web02/login.html')

def index(request):
    user_dict = request.session.get('is_login',None)
    if user_dict:
        return render_to_response('web02/index.html',{'username':user_dict['user']})
    else:
        return redirect('/web02/login/')

def logout(request):
    del request.session['is_login']
    return redirect('/web02/login')