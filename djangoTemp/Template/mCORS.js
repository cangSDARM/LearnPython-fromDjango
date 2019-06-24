//CORS: 跨域资源共享
//在发送AJAX时, 现代浏览器会自动解析跨域

TODO: 看的这本书没讲清楚, 之后自己百度再写

/*
	1. 发起跨域请求时, 引入额外的Origin头信息指定请求的源.
		Origin: http://request.com/
	2. 服务器检查头信息, 确定是否接收. 请求若被接收, 将返回Access-Control-Allow-Origin的头(值与Origin相同)
		Access-Control-Allow-Origin: http://request.com/
	3. 接收响应时, 浏览器检查ACAO头的值, 若与请求头中Origin的值不匹配, 则禁止该请求
 */