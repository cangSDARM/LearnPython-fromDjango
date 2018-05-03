# Django
### ProjectName
        |-  ProjectName             全局逻辑
        |       |-  __init__.py
        |       |-  settings.py     全局设置文件
        |       |-  urls.py         全局路径和函数绑定
        |       |-  wsgi.py         服务器使用WSGI部署的文件
        |-  application             app
        |       |-  admin.py
        |       |-  views.py        视图(模板语言, cookie)
        |       |-  apps.py
        |       |-  models.py       模型(数据库操作)
        |       |-  tests.py        测试(Form验证)
        |       |-  migrations
        |-  Template                模板
        |-  Statics                 JS,CSS,img等静态文件路径
        |-  Utils                   其它内容
        |       |-  message.py      邮箱/手机发送服务
        |       |-  CheckCode.py    验证码图片
        |-  db.sqlite3              数据库
        |-  manage.py               Django项目管理

### 流程
客户端 -> Urls -> Views
HTTP基于请求/相应, 无状态

#### MVC
* web分为:模型M, 控制器C, 视图V 三层;以松耦合式的方式链接
* 模型负责对象与数据库, 视图负责用户与页面, 控制器负责请求

#### MTV
* web分为:模型M, 模板T, 视图V 三层;以松耦合的方式链接
* 模型负责对象与数据库, 视图负责事件逻辑, 模板负责页面展示

## 初始化
* python3 django-admin.py startproject projectName 创建project
* python3 manage.py runserver ipdress port   通过端口启动服务器端
* python3 manage.py magrate    创建db.sqlite3(数据库)
* python3 manage.py createsuperuser     创建管理员allen/django030410
* python3 manage.py startapp appName   创建app
* python3 manage.py makemigrations 创造数据迁移
* python3 manage.py migrate 创建表结构, Django会自动添加一个id作为主键
* python manage.py clearsessions 清除session数据库

***

*响应头 ResponseHeaders*
> Content-Type:响应体使用编码
> Set-Cookie:响应给客户端的cookie
> Date:响应的时间

*请求头 RequestHeaders*
> User-Agent:用户浏览器和操作系统相关信息
> Accept:接受文档类型
> Accept-Encoding:支持的压缩格式
> Accept-Language:支持的语言
> Connection:链接方式,keep-alive默认3000ms
> Cookie:本地cookie信息
> Referer:从哪个页面跳转而来
> Content-Type:表单数据类型
> POST请求体:大小无上限,存在中文使用URL编码