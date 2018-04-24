//跨域请求
//浏览器同源策略: 域名, 端口, 协议相同. 不同源的客户端脚本未授权时不可以访问服务器资源
//前提条件: src属性可以跨域

//jsonp: json + padding
/*-------------------------------------原理
请求数据方:
前端:
    <script src="https://127.0.0.1:8000/scr"></script>
    <script>
        function test(d){
            alert(d)
        }
    </script>

发送数据方:
后端:
    def scr(req):
        return HttpResponse("test('data')")     //传输data
*/

/*--------------------------------------封装
前端:
    function addScript(scr){      //添加<script>标签
        var script = document.createElement("script");
        script.setAttribute("type", "text/javascript");
        script.src      //获取域名, 端口和协议
        document.body.appendChild(script);
    }
    window.onload = function(){   //测试
        addScript("https://127.0.0.1:8000/index?callback=fetch");   //如果有要求, 通过GET发送, 且只能发送GET请求
    }
    function fetch(arg){}    //调用数据函数
后端:
    def fun(req):
        func = req.GET.get("callback", None)
        data = ""
        return HttpResponse("%s(%s)"%(func,data))   //调用前端要求的callback函数
*/

/*--------------------------------------jQuary实现
前端:
----JSON:
    <script type="text/javascript">
        $.getJSON("https://127.0.0.1:8000/index?callback=?",function(arg){
            alert("回调函数执行");
        });
    </script>
----AJAX:
    ----固定函数名:
        <script type="text/javascript">
            $.getajax({
                url:"https://127.0.0.1:8000/index",
                dataType:"jsonp",
                jsonp:"callback",          //回调所需的索引值
                jsonpCallback:"fetch",      //回调函数名
            });
            function fetch(arg){}
        </script>
    ----自执行函数:
        <script type="text/javascript">
            $.getajax({
                url:"https://127.0.0.1:8000/index",
                dataType:"jsonp",
                jsonp:"callback",          //回调所需的索引值
                success:function(arg){}     //回调函数
            });
        </script>
后端:
    同上
*/