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


#------------------------------------------Cookie---------------------------------------
'''
1. 用于服务器验证用户, 提取用户相关信息
2. 保存于客户端的文件
3. 跨域cookie理论无法共享
'''
#-----------------------------------------简单cookie
def CookieSim(req):
    if(!req.COOKIES.get("Name")):        #获取Cookie
        rep = HttpResponse("/index")
        rep.set_cookie("Name", "alex", max_age=10, '''expires,'''path="/", domain="biadu.com", secure=True)
        #设置Cookie, 周期为10s(expires为ie5之前的), path为cookie生效URL, domin表示cookie生效域名, secure表示需要https

        rep.set_signed_cookie("On", "value", salt="密钥")    #设置签名cookie
        return rep
    if req.COOKIES.has_key('ON'):   #判断cookie是否存在
        req.COOKIES.get("Name") #获取cookie
    req.get_signed_cookie("On", salt="密钥") #获取签名cookie

    ia = requests.get("URL")    #登录页面获取cookie
    ia2 =  requests.post("URL", data={}, cookies=ia.cookies.get_dirt()) #用户登录,携带上次cookie,后台对cookie的gpsd授权
    gpsd = ia.cookies.get_dirt()['gpsd']    #操作
    ia3 = requests.post("URL", cookies={'gpsd'=gpsd})
#-----------------------------------------session
#  作用:(和cookie的区别)  敏感信息保存在服务器, 防止客户端修改cookie信息
#----------------------------相关操作
#.............增/改
#request.session['name'] = obj.username      #设置Session中数据
#request.session.setdefault('pwd',123)       # 存在则不设置
#request.session.set_expiry(value)          #设置session过期时间, 可以是秒数/具体时间/0(关闭浏览器session失效)/None(依赖全局session失效策略)
#.............查
#request.session.get('name', None)   #没有拿None
#request.session["k1"]              #如果不存在则会报错
#request.session.keys()
#request.session.values()
#request.session.items()
#request.session.iterkeys()
#request.session.itervalues()
#request.session.iteritems()
#request.session.session_key     # 用户session的随机字符串
#.............删
#del request.session['pwd']      #删除session中数据
#request.session.clear()        #清空
#request.session.clear_expired()     #将数据库里时间过期的session删除掉
#request.session.delete("session_key")   # 删除当前用户的所有Session数据
#----------------------------例子
def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        name = request.POST.get('user')
        pwd = request.POST.get('pwd')
        obj = models.Boy.objects.filter(username=name, passwprd=pwd).first()
        if obj:
            #1, 生成随机字符串（sessionID）
            #2, 通过cookie发送给客户端
            #3, 服务端保存{随机字符串:{'name':'value', 'pwd':123}}
            request.session['name'] = obj.username
            request.session.setdefault('pwd',123)
            return redirect('/index')
        else:
            return render(request,'login.html',{'msg':"用户名/密码错误"})

def index(request):
    #1, 获取客户端的 sessionID
    #2, 在服务端查找是否存在 这个sessionID
    #3, 在服务端查看对应的key sessionID键的值中是否有name(有值就是登录过了)
    v=request.session.get('name', None)
    if v:
        return render(request,'index.html',{'msg':v})
    else:
        return redirect('/login/')
'''
#-----------------------------------------客户端操作cookie
---------------------1. DOM
#document.cookie;
---------------------2. jQuary.cookie.js
    .创建
$.cookie('the_cookie', 'the_value', { expires: 7, path: '/' });    //7days
    .读取
$.cookie();
    .删除
$.removeCookie('the_cookie', null);
'''
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