//跨域请求
//浏览器同源策略: 域名, 端口, 协议相同. 不同源的客户端脚本未授权时不可以访问服务器资源
//前提条件: script的src属性可以跨域

//jsonp: json + padding
//是一种通过<script>加载JSON响应的模式.
//前端使用<script>访问请求一个js文件, 等文件加载完后自动执行.
//而服务器通过脚本url的查询字符串, 将响应封装在回调函数中.
//回调函数名是由请求方通过URL的查询字符串提供的. 这个回调函数被称作填充, 即JSONP的P

//缺点:
//  1. JSONP只能使用GET请求; 提交的数据量受URL最大长度限制
//  2. JSONP缺乏错误处理机制; 调用失败无任何响应, 只能前端设置超时检测处理
//  3. JSONP可能被进行跨站请求伪造(CSRF)攻击;
//  4. JSONP响应总是异步的; 没法改成同步阻塞;

/*--------------------------------------封装
前端:
    function addScript(scr){      //添加<script>标签
        var script = document.createElement("script");
        script.setAttribute("type", "text/javascript");
        console.log(script.src);      //获取域名, 端口和协议
        document.body.appendChild(script);
    }
    window.onload = function(){   //发送JSONP请求
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