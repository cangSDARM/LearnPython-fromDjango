from django.shortcuts import render
from django.http import HttpResponse
from mdjango import models
import os
import datetime
import requests

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
    HttpResponse.status_code = "404"    #模拟状态码错误
    return HttpResponse("articles,%d" % article) #返回文本内容

'''
------------------------------------------Cookie---------------------------------------
1. 用于服务器验证用户, 提取用户相关信息
2. 保存于客户端的键值对文件
3. 跨域cookie理论无法共享
'''
#--------------------------------------cookie模拟爬虫
def CookieSim(req):
    if(!req.COOKIES.get("Name")):        #获取Cookie
        rep = HttpResponse("/index")
        rep.set_cookie("Name", "alex", max_age=10, '''expires''', path="")      #设置Cookie, 周期为10s(expires为具体时间), path为生效路径

    ia = requests.get("URL")    #登录页面获取cookie
    ia2 =  requests.post("URL", data={}, cookies=ia.cookies.get_dirt()) #用户登录,携带上次cookie,后台对cookie的gpsd授权
    gpsd = ia.cookies.get_dirt()['gpsd']    #操作
    ia3 = requests.post("URL", cookies={'gpsd'=gpsd})
#--------------------------------------------------------------------------------------

#-----------------------------------------模板语言---------------------------------------
def temlateLangue(req):
    time = datetime.datetime.now()  #后端动态数据
    
    return render(req, "temp.html", {"d":time})
    #render(request, template, context)
    #   template:
    #       from django.template import Template
    #       t = Template("hello{{ name }}")
    #   context:
    #       from django.template import Context
    #       c = Context({"name": 123 })
    #t.render(c)    #hello123
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
-----------------------------------------过滤器
 前端:
    {{ 处理对象|相关方法|相关方法2 }}     #对处理对象执行相关方法, 可以拼接
    {{ s|add:"5" }}   #对s加5, 过滤器方法和参数之间用:隔开, 参数用""包裹
-----------------------------------------防治跨站攻击验证
 前端:
    {% csrf_token %}    #form表单需要
-----------------------------------------起别名
 前端:
    {% with f=slllllllllllllijweo %}  #和python的with用法相同
    {{ f }}
    {% endwith %}
-----------------------------------------转义
 前端:
    {% verbatim %}
    {{ value }}
    {% endverbatim %}
-----------------------------------------渲染后端标签
 前端:
    1.
    {% autoescape off %}
    {{ value }}
    {% endautoescape %}
    2.
    {{ value|safe }}
-----------------------------------------逻辑判断
 前端:
    {% if 只能是bool值明确的语句,不能判断 可以用not and or%}
    {% elif ... %}
    {% else ... %}
    {% endif %}
-----------------------------------------模板比较
 前端:
    {% ifequal/ifnotequal value1 value2 %}
    {% else %}
    {% endifequal %}
-----------------------------------------循环替换
 发送:
    {"list":list}
 前端:
    {% for i in list %}
        {{ forloop.counter }}   #循环次数, 从一开始
        {{ forloop.counter0 }}   #循环次数, 从零开始
        {{ forloop.revcounter }}   #循环次数, 翻转计数
        <tr>
            <td>{{i.username}}</td>
            <td>{{i.sex}}</td>
            <td>{{i.email}}</td>
        </tr>
    {% endfor %}
    {{ list.2 }}    #4, 后端的属性/数组/字典/元祖等负杂数据结构都可以通过.调用
 后端:
    list = [
        {"username":"xxx", "sex":1, "email":000}, 
        {"username":"yyy", "sex":1, "email":111},
        4,
    ]
-----------------------------------------注释
 前端:
    {# 内容 #}
-----------------------------------------自定义
 tmplatetags/simple_tags.py
-----------------------------------------模板的继承
 Template/base.html
'''