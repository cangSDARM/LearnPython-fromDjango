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


## 初始化
* python3 manage.py runserver   启动服务器端
* python3 manage.py magrate    创建db.sqlite3(数据库)
* python3 manage.py createsuperuser     创建管理员allen/django030410
* python3 manage.py startapp appName   创建app
* python3 manage.py makemigrations 创造数据迁移
* python3 manage.py migrate 迁移