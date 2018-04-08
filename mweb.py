#简单web框架
#WSGI: web server gatway interface
from wsgiref.simple_server import make_server

def application(environ, start_response):   #environ请求头dirt
    start_response('200 OK', [('Content-Type', 'text/html')])   #相应头
    return [b'<h1>hello world</h1>']

httpd = make_server('', 8000, application)
print("running http on 8000....")
httpd.serve_forever()   #开始监听
