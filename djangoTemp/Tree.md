# Django
### ProjectName
        |-  ProjectName             包
        |       |-  __init__.py
        |       |-  settings.py     全局设置文件
        |       |-  urls.py         全局路由控制
        |       |-  wsgl.py         服务器使用wsgi部署的文件
        |-  manage.py               Django项目管理

### 流程
客户端 -> Urls -> Views
HTTP基于请求/相应, 无状态

## 初始化
* python3 manage.py runserver   启动服务器端
* python3 manage.py magrate    创建db.sqlite3(数据库)
* python3 manage.py createsuperuser     创建管理员allen/django030410
* python3 manage.py startapp appName   创建app
* python3 manage.py makemigrations 创造数据迁移
* python3 manage.py migrate 迁移

***

*相应头 ResponseHeaders*
    Content-Type:响应体使用编码
    Set-Cookie:响应给客户端的cookie
    Date:响应的时间
*请求头 RequestHeaders*
    User-Agent:用户浏览器和操作系统相关信息
    Accept:接受文档类型
    Accept-Encoding:支持的压缩格式
    Accept-Language:支持的语言
    Connection:链接方式,keep-alive默认3000ms
    Cookie:本地cookie信息
    Referer:从哪个页面跳转而来
    Content-Type:表单数据类型
    POST请求体:大小无上限,存在中文使用URL编码