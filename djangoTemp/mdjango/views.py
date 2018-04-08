from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
import os
import datetime

# Create your views here.
def func(req):  #req 请求头
    print('request %s' %req.GET)     #获取from表单get数据
    print('request %s' %req.POST)    #post
    print('file %s' %req.FILES)      #上传文件时的单独封装

    for item in req.FILES:
        obj = req.FILES.get(item)
        fileName = obj.name
        f = open(fileName,'wb')
        for line in obj.chunks():   #分段取数据
            f.write(line)
        f.close()

    return render(req, 'index.html')     #渲染网页并返回, 第一个参数必须为请求头

def Article_D(request, article):
    return HttpResponse("articles,%d" % article) #返回文本内容

#模板语言
def temlateLangue(req):
    time = datetime.datetime.now()  #后端动态数据
    
    return render(req, "temp.html", {"d":time})
    # 前端:{{d}}
    # 后端:time
    # d就可以动态替换为time
