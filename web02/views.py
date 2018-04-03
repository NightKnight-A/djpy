# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response,redirect

# Create your views here.

def login(request):
    if request.method == 'POST':
        user = request.POST.get('username',None)
        pwd = request.POST.get('password',None)
        if user == 'alex' and pwd == '123':
            request.session['is_login'] = True
            return redirect('/web02/index/')
        else:
            return render_to_response('web02/login.html',{'msg':'用戶名或密碼錯誤。'})
    return render_to_response('web02/login.html')

def index(request):
    is_login = request.session.get('is_login',None)
    if is_login:
        return render_to_response('web02/index.html')
    else:
        return redirect('/web02/login/')
