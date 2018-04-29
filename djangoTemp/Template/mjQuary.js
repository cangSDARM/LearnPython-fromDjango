//如果是jquary对象,需在变量名前加$
//语法类似css, 支持链式操作

jQuary; //jQuary对象, 可以简写为$

//参考文档: jquary.cuishifeng.cn/

/*
 ----------------------- 选择器 ----------------------
 *基本
 *  $("*") $("#id") $(".class") $("p,div")
 *层级
 *  $(".outer div") $(".outer > div") $(".outer+div")
 *  $(".outer~div")---------->向下找寻同级div
 *属性
 *  $("[id="div1"]") $("["xd"="11"][id]")
 *表单(只适用于input标签)
 *  $("[type="text"]") == $(":text")
 ----------------------- 筛选器 -----------------------
 *基本
 *  $("li:first") $("li:even")
 *  $("li:gt(1)")--------------->查找序号大于2的
 *  $("li:lt(2)")--------------->查找序号小于2的
 *  $("li:eq(2)")--------------->查找序号为2的
 *过滤
 *  $("li").first() $("li").eq(2) $("ul li").hasclass("test")
 *查找
 *  $("div").children(".test")
 *  $("div").find(".test")--------------->查找所有后代
 *  $(".test").next() $(".test").nextAll() $(".test").netUntil()
 *  $("div").prev() $("div").prevAll() $("div").prevUntil()
 *  $(".test").parent() $(".test").parents() $(".test").parentUntil()
 *  $("div").siblings()
*/

//jquary事件
$("parent").on("event", "object", function(){
    //实现动态绑定event
});

//jquary循环
$.each(loopArray, function(index, value){
    console.log(index + ":" + value);
})
$.each(loopDic, function(key, value){
    console.log(key + ":" + value);
})
$("ul li").each(function(){
    $(this).val("loop");   //==this.value
})

$("#test").html();  //== document.getElementById("test").innerHTML;
$("*").css("color","red").css("background","yellow");  //修改css

//扩展方法
(function($){
    //扩展方法通常写在自执行函数内, 扩展方法之间的全局变量可以不影响其它函数(私有域)
    //不写在自执行函数内也可以,但不推荐
    $.extend({
        functionName:function(){
            return 0;
        }
    });

    //需要找到节点才可调用
    $.fn.extend({
        print:function(){
            console.log($(this).html());    //打印内容
        }
    });
})(jQuary);

$.functionName();   //调用
$("p").print();     //调用
