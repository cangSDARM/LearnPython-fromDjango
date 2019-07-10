## 永远返回HttpResponse
## 或者返回JsonResponse, 就不用dumps了
`pip install djangorestframework`

## RESTful Front

## RESTful Back

### 认证
```python
from rest_framework.views import APIView
from rest_framework import exceptions
class MAuthentication(object):
    def authenticate(self, request):
        # rest_framework包装了request, request对象触发验证
        token = request._request.GET.get("token"))    #原生request
        if not token:
            #前端需要: /api/XXX/?token=XXX
            raise exceptions.AuthenticationFailed("用户认证失败")     #发送失败json: {"detail":"用户认证失败"}
        return ("user", None)   #使用: (request.user, request.auth)

    def authenticate_header(self):
        pass
```
### View部分
```python
class MView(APIView):
    authentication_classes = [MAuthentication]
    def get(self, request, *args, **kwargs):
        # 先通过dispatch分发, 封装request, 读取验证类
        # 之后通过MAuthentication验证
        return HttpResponse(json.dumps({code:"0"}), status=200)
```