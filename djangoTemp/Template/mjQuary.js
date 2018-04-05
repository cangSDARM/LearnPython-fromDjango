//如果是jquery对象,需在变量名前加$
//语法类似css, 支持链式操作

jQuary; //jQuary对象, 可以简写为$

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

$("#test").html();  //== document.getElementById("test").innerHTML;
$("*").css("color","red").css("background","yellow");  //修改css
