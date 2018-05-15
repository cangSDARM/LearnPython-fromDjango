
#----------------------------------------------中间件------------------------------------------------------
#|          用途:            在用户访问url或views前后提供操作或检查
#|          访问生命周期:     用户->中间件->url->views->中间件->用户
#|          位置:            settings.py里的MIDDLEWARE就是中间件(其顺序就是访问时中间件调用顺序, 返回时相反)
#---------------------------------------------------------------------------------------------------------
try:
    from django.utils.deprecation import MiddlewareMixin  # Django higher
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x lower

#添加: MIDDLEWARE里加"mdjango.Middleware.CommentMiddleWare"
class CommentMiddleWare(MiddlewareMixin):
    def __call__(self, request):    #本质, 可以不用继承MiddlewareMixin
        response = None
        if hasattr(self, 'process_request'):
            #执行当前的process_request
            response = self.process_request(request)
        if not response:
            #执行下一个的__call__
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            #执行当前的process_response
            response = self.process_response(request, response)
        return response

    def process_request(self, request):         #访问views
        pass
    def process_response(self, request, response):  #返回用户
        return response     #必须返回response