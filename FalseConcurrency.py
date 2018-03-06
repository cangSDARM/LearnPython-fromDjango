#并发,框架.客户端毫无变化
import socketserver

class Myserver(socketserver.BaseRequestHandler):
	def setup(self):	#准备工作
		pass

	def finish(self):	#结束工作
		pass

	def handle(self):
		while True:
			conn = self.request
			print(self.client_address)
			while True:
				client_data = conn.recv(1024)
				print(str(client_data,'ut8'))
				conn.sendall(client_data)
			conn.close()

if __name__ == '__main__':
	server = socketserver.ThreadingTCPServer(('127.0.0.1',8091),Myserver)	#链接
	server.serve_forever()	#启动
