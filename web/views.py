# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response

from web import models
from web import common
from django.utils.safestring import mark_safe
from web import html_helper
# Create your views here.

def index(request,page):
    page = common.try_int(page,1)
    count = models.Host.objects.all().count()

    pageObj = html_helper.PageInfo(page,count)

    result = models.Host.objects.all()[pageObj.start:pageObj.end]

    page_string = html_helper.Pager(page,pageObj.all_pages_count)

    ret = {'data':result,'count':count,'page':page_string}

    response = render_to_response('index.html',ret)

    response.set_cookie('k1','v1')

    return response