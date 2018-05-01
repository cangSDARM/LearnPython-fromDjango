from django.test import TestCase

# Create your tests here.
#-------------------------------Django Form验证-----------------------------------
#|      简化后端验证步骤     |
#-------------------------------定义模板
from django import forms
class Form(forms.Form):
    user = forms.CharField(min_length=6)    #前端form的name必须和属性名一致
    email = forms.EmailField(error_messages={'requird':"空错误", 'invalid':"格式错误", 'min_length':"长度限制错误"}) #自定义错误信息, key值Django内部定义
    favor = forms.ChoiceField(choices=[(1, "value1"), (2, "value2")])    #下拉框
    sport = forms.MultipleChoiceField()     #多选框
#-------------------------------使用模板
def Login(request):
    if request.method == "GET":
        myform = Form()
        return redirect(request, "login", {'form':myform})  #前端自动生成form的input标签, 保留输入数据
    if request.method == "POST":
        myform = Form(request.POST) #自动校验, 可以传字典
        current = myform.clean()     #只返回校验成功的键值, 返回字典
        myerrors = myform.errors.as_json()  #拿取校验错误的键值和信息, (as_ul, as_json, as_data, as_text)
        if myform.is_valid():    #全部校验成功
            pass
        else:   
            #前端两次反序列化: ret["error"] = myform.errors.as_json()
            #前端一次反序列化
            ret = ["error":None, "data":None}]
            ret["error"] = myform.errors.as_data()
            return HttpResponse(json.dumps(ret, cls=JsonDump))

class JsonDump(json.JSONEncoder):
    def default(self, field):
        from django.core.exceptions import ValidationError
        if isinstance(field, ValidationError):
            return {"code":field.code, "message":field.message}
        else:
            return json.JSONEncoder.default(self, field)