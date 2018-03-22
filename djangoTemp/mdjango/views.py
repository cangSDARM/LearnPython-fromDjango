from django.shortcuts import render

from django.http import HttpResponse

def func(request):
    return HttpResponse("Hello, world")     #返回文本内容
# Create your views here.
