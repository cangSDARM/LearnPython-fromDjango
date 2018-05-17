'''
-----------------------------------------缓存--------------------------------------------------------------
|                  用处: 提高用户访问速度                                              |
|                  本质: 字典保存数据                                                 |
|                  原理: 将需要读取的数据先存在内存里, 用户大量访问时不通过view而是缓存       |
-----------------------------------------------------------------------------------------------------------
--------------------------Django提供6种缓存方式配置:
    开发调试
        CACHES = {
            'default':{
                'BACKEND': 'django.core.cache.backends.dummy.DummyCache', #引擎
                'TIMEOUT': 300, #缓存更新时间间隔(None永久, 0立即)
                'OPTIONS':{
                    'MAX-ENTRIES': 300   #最大缓存个数
                    'CULL_FREQUENCY': 3, #缓存占满后, 按1/CULL_FREQUENCY比例删除缓存
                },
                'KEY_PREFIX': '',    #缓存key的前缀
                'VERSION': 1,    #key的版本
                'KEY_FUNCTION': FUNC,    #生成key的函数
            }
        }
    内存
        CACHES ={
            'default:{
                'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
                'LOCATION': 'unique-snowflake', #缓存名
            }
        }
    文件
        CACHES ={
            'default:{
                'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
                'LOCATION': '/var/temp/django_temp',
            }
        }
    数据库
        执行: python3 manage.py createcachetable
        CACHES ={
            'default:{
                'BACKEND': 'django.core.cache.backends.db.DataBaseCache',
                'LOCATION': 'cache_table',  #表名
            }
        }
    Memcache缓存(python-memcached模块)
        CACHES ={
            'default:{
                'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
                'LOCATION': '127.0.0.1:11001',  #ip:port,
                #'LOCATION': 'unix:/tmp/memcached.sock',    #自己文件里写socket信息
                #'LOCATION': ['127.0.0.1:1011', '127.0.0.2:233'],
            }
        }
    Memcache缓存(python-mc模块)
        CACHES ={
            'default:{
                'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
                'LOCATION': 'unix:/tmp/memcached.sock',
            }
        }

--------------------------KEY函数
    def default_key_func(key, key_prefix, version):
        return '%s:%s:%s' %(key_prefix, version, key)

--------------------------应用
    全局缓存
    MIDDLEWARE ={
        'django.Middleware.cache.UpdateCacheMiddleware',        #view之后:判断缓存是否存在, 更新缓存
        其它中间件
        'django.Middleware.cache.FetchFromCacheMiddleware',     #view之前:认证用户, 确认缓存内容, 获取内容直接返回
    }
    CACHE_MIDDLEWARE_ALIAS = ""
    CACHE_MIDDLEWARE_SECONDS = ""
    CACHE_MIDDLEWARE_KEY_PREFIX = ""
    单独的View缓存
    1.
        from django.views.decorators.cache import cache_page
        @cache_page(60*15)  #超时时间
        def viewer(request):
            pass
    2.
        from django.views.decorators.cache import cache_page
        urlpatterns = [
            url(r'^admin', cache_page(60*15)(viewer)),
        ]
    局部页面缓存
    {% load cache%} #加载cache的tag
    {% cache 500 keyName %} #500:超时时间, keyName:缓存key名
        content
    {% endcache %}
'''
