"""djangoTemp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf   路由分发, 将同一功能网址分配到指定的结构相同的py文件里.
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from mdjango import views

urlpatterns = [
    #url(正则表达式, 处理函数, 参数, 别名)
#处理函数添加参数:
    #通过正则表达式
    #1 包含组(用括号括的内容), 视作str参数
    #2 包含(?<groupname>正则表达式),则参数以 groupname为参数名传递
    #通过参数
    #1 字典:{"paramname":value},则参数以 paramname为参数名传递
#别名:
    #name="Articles"表示路径的别名,防止后台更改引起前端更改.前端写法: {% url "Articles" %}
    
    url(r'^admin/', admin.site.urls),   #后台管理页
    #url(r'^login$', views.loginClass.as_view()),     #绑定类
    url(r'^index', views.func),  #通过index网页访问, views.func处理响应
    url(r'article/<int:article>', views.Article_D, name='Articles'),    #传入参数:int article和定义时相同名称
]
