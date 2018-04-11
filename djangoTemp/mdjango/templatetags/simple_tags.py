#自定义过滤器
#1. 在 自定义的app 路径下创建 templatetags文件
#2. 创建.py文件

from django import template
from django.utils.safestring import mark_safe
register = template.Library()   #register为固定变量名, 不可改变

@register.simple_tag    #调用不需要管道符, 函数与参数用space隔开
def simpletag():        #{% simpletag %}
    pass                #不能用于模板语言的if/for

@register.filter        #需要管道符, 函数与参数用:隔开, 最多两个参数
def simplefilter():     #{{ value|simplefilter }}
    pass

#4. 前端导入: {% load simple_tags %}