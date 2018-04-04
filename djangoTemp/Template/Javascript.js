/*Js基于对象
 -核心: EcmaScript, Java
 -文档对象模型(Document Object Model)
 -浏览器对象模型(Browser Object Model)
 -描述文件: .d.ts
*/

/* 数据类型(自动转换且不报错)
 * 基础数据类型
    * Number: int/float
    * Null: null
    * Undefined: undefind
    * String: ""
    * Boolean: true/false
 * 复杂数据类型
    * var a = [ 1, 2, 3, "sse"];   //数组
    *     for(var i in a);    //i取a的下标
    *     a.shift/a.unshift   //从栈底操作
    *     a.push/a.pop        //从栈顶操作
    * var b = { 2:2, 3:3, 4:3};  //类似字典
    *     for(var i in b);    //i取key
    * var c = (1, 2, 34, 5);     //元祖
    * var d = new Date();     //现在的时间
    * var e = new RegExp("规则", "模式(g:全局通用; i:不区分大小写)");     //正则表达式
    * var e = /规则/模式
    *     e.text("需要匹配的字符串")    //boolean
    *     string.match(e)           //arrary
    *     string.search(e)           //index
 * 一些(为真)逻辑表达
    * (NaN表达式一定为false)
    * null == undefined
    * NaN != NaN
    * "5" == 5
    * 字符串比ASCII码
*/

x = 2;      //全局变量

function functionName(){
    //js参数随便传, 通过arguments参数(数组)对象获取动态传入的参数
    arguments.length;

    var y = 0x2;      //不用var是全局变量
    parseInt("1.12a");   //转换成int, string转换失败时出现NaN

    var res = ["hello", "js", "world"].join("..")   //res="hello..js..world"
    //python: res = "..".join(['hello', 'js', 'world'])

    typeof(y);      //查看数据类型, 用new的对象检测永远是object
    y instanceof String;    //判断是否是String对象
    
    return 0;
}

//其它的函数声明形式
var func2 = new Function("参数1","参数2", "参数3", "函数内容");

functionName.length     //参数个数
void(functionName());   //void 返回undefined

//匿名函数
var func1 = function(args){
    return "func1";
}
func1();
//自执行函数
(function(args){
    return(arguments.length);
})(1,2,3)

/*-----------------------------------------BOM----------------------------------------------------*/
//浏览器对象模型, 对浏览器窗口进行访问和操作

//window: 一个html文件对应一个window对象
console.log(x);     //控制台输出
window.alert(x);       //弹窗, 实际对于window而言是个全局对象所以可以省略window, 直接使用alert()
confirm("消息");          //显示有确认/取消按钮的对话框
prompt("提示");           //显示可提示用户输入的对话框
open();             //打开一个新窗口或查找窗口
close();
var id = setInterval(functionName, time);      //按照指定周期调用函数或表达式
clearInterval(id);
var id = setTimeout(functionName, time);       //在指定时间后调用函数或表达式
clearTimeout(id);
scrollTo();         //将内容滚动到指定坐标

//history: 包含用户访问过的URL
history.length();   //历史URL数量
history.forward();  //向前
history.back();
history.go();       //直接跳(-1:back, 1:forword)

//location: 包含当前URL的信息
location.reload(forceReload)   //刷新
location.href       //返回当前页面的 URL 或跳转
location.hostname   //返回 web 主机的域名
location.pathname   //返回当前页面的路径和文件名
location.port       //返回 web 主机的端口 （80 或 443）
location.protocol   //返回所使用的 web 协议（http:// 或 https://）
location.pathname   //返回 URL 的路径名
location.assign()   //加载新的文档

//screen: 包含有关用户屏幕的信息
screen.availWidth   //可用的屏幕宽度
screen.availHeight  //可用的屏幕高度

//navigator: 包含有关访问者浏览器的信息, 可以被篡改

/*----------------------------------------DOM--------------------------------------------------------*/
//文档对象模型, 对html文档的标签和内容进行操作
//文档: document, 标签: element, 属性: attribute, 文本: text, 注释: comment
// html的DOM 和 XML的DOM 相同
var re = document.getElementById("Id");
re.value = "id";           //id的value属性

//Event
/*两种绑定event方法
1. 直接写在标签里, 有返回时需: return + functionName
2. document.getElementById("id").onsubmit = function check(){}
*/
initEvent();	    //初始化新创建的 Event 对象的属性
preventDefault();	//通知浏览器不要执行与事件关联的默认动作, 通常阻止数据发向后端
stopPropagation();	//不向外派发事件, 通常防止鼠标穿透
onclick;    //单击
ondblclick; //双击
onfocus;    //获取焦点(Ins)
onblur;     //失去焦点(Ins)
onchange;   //域的内容被改变
onkeypress; //按住
onkeydown;
onkeyup;
onload;     //完成加载
onmousedown;
onmousemove;
onmouseover;
onmouseout;
onselect;   //文本被选中
onsubmit;   //被提交, 只能绑在form标签

/*对html标签的增删改查
 *增
 *  document.createElement();
 *  document.appendChild();
 *删
 *  parentElement.removeChild();
 *改
 *  setAttribute();
 *  innerHTML;
 *  innerText;  //不能渲染
 * 改CSS
 *  ele.style.fontSize="30px";
 *查
 *  document.getElementById();
 */
