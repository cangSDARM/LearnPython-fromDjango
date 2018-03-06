import socket
import os


def Chat():
	print('*'*20+'Chat'+'*'*20)
	while True:
		inp = input('>>>')
		if inp == 'exit':
			return
		sk.send(bytes(inp, 'utf8'))
		data = sk.recv(1024)
		print(str(data, 'utf8'))


def Controal():
	print('*'*20+'Control'+'*'*20)
	while True:
		inp = input('>>>')
		if inp == 'exit':
			return
		sk.send(bytes(inp, 'utf8'))
		lens = int(str(sk.recv(1024), 'utf8'))
		print(lens)
		sk.send('00')
		std = bytes()
		while len(std) != lens:
			std += sk.recv(1024)
		print(str(std, 'utf8'))


def UploadFile():
	print('*'*20+'Upload'+'*'*20)
	while True:
		inp = input('>>>').strip()
		if inp == 'exit':
			return
		cmd, path = inp.split('|')
		if cmd != 'post':
			continue
		path = os.path.join(DIR, path)
		filename = os.path.basename(path)
		filesize = os.stat(path).st_size
		fileinfo = 'post|%s|%s' % (filename, filesize)
		sk.sendall(bytes(fileinfo, 'utf8'))

		f = open(path, 'rb')
		hassent = 0
		while hassent != filesize:
			data = f.read(1024)
			sk.sendall(data)
			hassent += len(data)
		f.close()


if __name__ == "__main__":
	sk = socket.socket()
	address = ('127.0.0.1', 8008)
	sk.connect(address)
	DIR = os.path.dirname(os.path.abspath(__file__))
	while True:
		print("1,chat\n2,upload file\n3,control servicer\n0,exit client\nexit,exit servicer")
		inp = input('>>>')
		sk.send(bytes(inp, 'utf8'))
		if inp == '0' or inp == 'exit':
			break
		elif inp == '1':
			Chat()
		elif inp == '2':
			UploadFile()
		elif inp == '3':
			Controal()
		continue
	sk.close()
