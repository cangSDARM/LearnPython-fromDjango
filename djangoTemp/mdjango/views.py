from django.shortcuts import render
from django.http import HttpResponse
from mdjango import models
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
    #return render_to_response('index.html')    #和render类似
    #return redirect('/index')  #函数跳转, 通过urls的路径跳转到相关函数

def Article_D(request, article):
    return HttpResponse("articles,%d" % article) #返回文本内容

'''
#-------------------------------数据库操作-------------------------------
# ------------------------------增
#1
    models.Article.objects.create(
        title = "e",text = "t",)
#2
    test1 = models.Article(title='runoob', text='file')
    test1.save()
# ------------------------------删
# 删除id=1的数据
#1
    test1 = models.Article.objects.get(id=1)
    test1.delete()
#2
    # models.Article.objects.filter(id=1).delete()
# 删除所有数据
    # models.Article.objects.all().delete()
# ------------------------------改
# 修改id=1的title字段, 再save, 相当于 UPDATE
#1
    test1 = models.Article.objects.get(id=1)
    test1.title = 'Google'
    test1.save()
#2
    #models.Article.objects.filter(id=1).update(title='Google')
# 修改所有的列
    # models.Article.objects.all().update(title='Google')
# ------------------------------查
# 获得所有数据, 相当于 SELECT * FROM
    list = models.Article.objects.all()        
# filter相当于 WHERE
    response2 = models.Article.objects.filter(id=1) 
# 获取单个对象
    response3 = models.Article.objects.get(id=1)     
# 限制返回的数据 相当于 OFFSET 0 LIMIT 2;
    models.Article.objects.order_by('title')[0:2]
# 数据排序
    models.Article.objects.order_by("id")
#---------------------------------------------------------------------------------------
'''

#-----------------------------------------模板语言---------------------------------------
def temlateLangue(req):
    time = datetime.datetime.now()  #后端动态数据
    
    return render(req, "temp.html", {"d":time})
    #return render(req, "temp.html", locals())  #使用locals()传递所有函数内部变量,前端直接使用本地变量名指代
'''
-----------------------------------------单个替换
 发送:
    {"d":time}
 前端:
    {{d}}
 后端:
    time
 d就可以动态替换为time

-----------------------------------------循环替换
 发送:
    {"list":list}
 前端:
    {% for i in list %}
        <tr>
            <td>{{i.username}}</td>
            <td>{{i.sex}}</td>
            <td>{{i.email}}</td>
        </tr>
    {% end for %}
 后端:
    list = [
        {"username":"xxx", "sex":1, "email":000}, 
        {"username":"yyy", "sex":1, "email":111},
    ]
-----------------------------------------注释:
 前端:
    {# 内容 #}
'''