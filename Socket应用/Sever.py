import socket
import os
import subprocess


def Chat(conn):
	while True:
		try:
			data = conn.recv(1024)
		except Exception:
			return
		if not data:
			return
		print(str(data, 'utf8'))
		inp = input('>>>')
		conn.send(bytes(inp, 'utf8'))


def Controal(conn):
	while True:
		try:
			data = conn.recv(1024)
		except Exception:
			return
		if not data:
			return
		print(str(data, 'utf8'))
		sb = subprocess.Popen(str(data, 'utf8'), shell=True, stdout=subprocess.PIPE)
		cmdout = sb.stdout.read()
		cmdlen = str(len(cmdout))
		conn.send(bytes(cmdlen, 'utf8'))
		conn.recv(1024)
		conn.sendall(cmdout)


def RecvFile(conn):
	while True:
		DIR = os.path.dirname(os.path.abspath(__file__))
		try:
			data = conn.recv(1024)
		except Exception:
			return
		if not data:
			return
		cmd, filename, filesize = str(data, 'utf8').split('|')
		path = os.path.join(DIR, filename)
		if cmd == 'post':
			filesize = int(filesize)
			f = open(path, 'ab')
			hasrecv = 0
			while hasrecv != filesize:
				data = conn.recv(1024)
				f.write(data)
				hasrecv += len(data)
			f.close()
		else:
			print('Upload had been false')


if __name__ == "__main__":
	sk = socket.socket()
	address = ('127.0.0.1', 8008)
	sk.bind(address)
	sk.listen(3)
	sk.settimeout(5)
	sk.setblocking(True)
	while True:
		conn, addr = sk.accept()
		print(conn+'has connected')
		try:
			choise = str(conn.recv(1024), 'utf8')
		except Exception as e:
			print(e)
			choise = '0'
		finally:
			if choise == '1':
				Chat(conn)
			elif choise == '2':
				RecvFile(conn)
			elif choise == '3':
				Controal(conn)
			elif choise == 'close':
 				break
		continue
	sk.close()
