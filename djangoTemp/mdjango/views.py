from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
import os

def func(req):
    print('request %s'%req.GET)     #获取from表单get数据
    print('request %s'%req.POST)    #post
    print('file %s'%req.FILES)      #上传文件时的单独封装

    for item in req.FILES:
        obj = req.FILES.get(item)
        fileName = obj.name
        f = open(fileName,'wb')
        for line in obj.chunks():   #分段取数据
            f.write(line)
        f.close()

    return render(req, 'index.html')     #渲染网页并返回

# Create your views here.
def Article_D(request, article):
    return HttpResponse("articles,%d" % article) #返回文本内容
