'''
-------------------------------------------------信号------------------------------------------------------
|                               实质: Django预留的钩子函数
|                               调用: 除有注释外, 信号都是自动触发
-----------------------------------------------------------------------------------------------------------
Management signals
    pre_migrate             #执行migrate命令前
    post_migrate            #执行migrate命令后

Model signals(from django.db.models.signals import)
    pre_init                #model执行其构造方法前
    post_init               #model执行其构造方法后
    pre_save                #model对象保存前
    post_save               #model对象保存后
    pre_delete              #model对象删除前
    post_delete             #model对象删除后
    m2m_changed             #model使用many2many操作第三张表(add, remove, clear)前后
    class_prepared          #程序启动时, 检测注册的每一个类时

Request/Response signals(from django.core.signals import)
    request_started         #请求到来前
    request_finished        #请求结束后
    got_request_exception   #请求异常后

Test signals(from django.test.signals import)
    setting_changed         #使用text测试修改配置文件时
    template_rendered       #使用text测试渲染模板时

Database signals(from django.db.backends.signals import)
    connection_created      #创建数据库连接时

钩子的注入(链接函数)
    def callback(sender, **kwargs):     #sender:调用参数
        print('callback')
        print(sender, kwargs)

    xx.connect(callback)    #xx:信号名
'''
