//Js基于对象
//核心EcmaScript
//文档对象模型(Document Object Model)
//浏览器对象模型(Browser Object Model)

/* 数据类型
 * 基础数据类型
    * Number: int/float
    * Null: null
    * Undefined: undefind
    * String: ""
    * Boolean: true/false
 */

x = 2;      //全局变量
alert(x);       //弹窗
console.log(x);     //控制台输出

function functionName(){
    var y = 0x2;      //不用var是全局变量
    parseInt("1.12a");   //转换成int, string转换失败时出现NaN(NaN表达式一定为false)
    typeof(y);      //查看数据类型
    return 0;
}