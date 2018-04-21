/*
    Asynchronous Javascript And XML(异步JS和XML)
    优点_使用js与服务器进行异步交互, 传输XML格式数据, 且交互时局部刷新网页
    缺点_需要处理浏览器兼容问题, 发送请求增多增加服务器压力
*/

/**
 *  -------------------------------局部刷新模拟
 * 
 * window.onload = function(){  //当文档加载完毕时执行
 *     var form = document.getElementById("form1")  //获取表单
 *     form.onsubmit = function(){  //监听表单提交
 *         var user = form.username.value;  //获取表单元素
 *         if(!user){
 *             var userSpan = document.getElementById('userSpan')   //获取span元素
 *             userSpan.innerText = '用户名不能为空';
 *             return false;    //标示拦截表单提交
 *         }
 *         return true;
 *     }
 * }
 */

// --------------------------------四步操作
//1. 创建核心对象(XMLHTTPRequest)
function creatXMLHttpRequest(){
    var xmlHead;
    try{
        xmlHead = new XMLHttpRequest();
    }catch(e){
        //适用于IE6
        try{
            xmlHead = new ActiveXObject("Msxm12.XMLHTTP");
        }catch(e){
            //适用于IE更早版本
            xmlHead = new ActiveXObject("Microsoft.XMLHTTP");
        }
    }
    return xmlHead;
}
var xmlHttpRequest = creatXMLHttpRequest();
//2. 使用核心对象打开与服务器链接
xmlHttpRequest.open("POST", "/index", true);    //open(请求方式, URL, 是否异步)
//3. 发送请求 [-Get请求:send(null)-]
xmlHttpRequest.send(null);      //send(请求体)
//4. 注册监听, 监听服务器响应
xmlHttpRequest.onreadystatechange = function(){ // 指定监听函数, 在对象状态发生变化时调用,执行4次!
    //readyState[查看对象状态, 4标示监听响应结束]
    //status[服务器响应状态码, 服务器响应结束后才有]
    if(xmlHttpRequest.readyState == 4 && xmlHttpRequest.status == 200){
        var date = xmlHttpRequest.responseText;     //获取服务器响应体
    }
};
