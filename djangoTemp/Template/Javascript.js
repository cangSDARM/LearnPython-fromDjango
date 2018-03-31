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
    * var b = { 2:2, 3:3, 4:3};  //类似字典
    *     for(var i in b);    //i取key
    * var c = (1, 2, 34, 5);     //元祖
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

//void 返回undefined
function functionName(){
    var y = 0x2;      //不用var是全局变量
    parseInt("1.12a");   //转换成int, string转换失败时出现NaN
    typeof(y);      //查看数据类型
    
    return 0;
}
