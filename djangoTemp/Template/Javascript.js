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
alert(x);       //弹窗
console.log(x);     //控制台输出

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
