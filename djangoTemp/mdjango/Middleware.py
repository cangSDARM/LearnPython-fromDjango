
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
    
    def process_view(self, request, view_func, view_args, view_kwargs):  #路由匹配(所有process_request执行完后再按顺序调用process_view)
        pass
    
    def process_template_response(self, request, response): #render渲染时匹配.html
        pass

    def process_exception(self, request, exception):    #异常处理(处理views异常)
        pass

    def process_response(self, request, response):  #返回用户
        return response     #必须返回response
#----------------------------------------------------------------------------------------------------------

#------------------------------------------CSRF跨站信息伪造--------------------------------------------------
#|                  原理: get请求发送凭证 -> 提交post请求 -> CSRF验证
#|                  views里必须用render
#|                  Ajax里
#|                      function csrfSafeMethod(method){    //只是POST提交时加csrftoken
#|                          return (/^(GET|HEAD|OPTIONS|TRACE)$/.text(method));
#|                      }
#|                      $.ajaxsetup({       //为所有ajax提交添加csrftoken
#|                          beforeSend:function(xhr, settings){
#|                              if(!csrfSafeMethod(settings.type)&& !this.crossDomain) xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
#|                          }
#|                      });
#----------------------------------------------------------------------------------------------------------
