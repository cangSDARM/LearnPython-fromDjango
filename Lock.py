'''
import threading
import time
class MyThread(threading.Thread):
	def doA(self):
		Lock.acquire()
		print('gotA',time.ctime())
		time.sleep(1)
		Lock.acquire()
		print('gotB',time.ctime())
		Lock.release()
		Lock.release()
	
	def doB(self):
		Lock.acquire()
		print('gotB',time.ctime())
		time.sleep(2)
		Lock.acquire()
		print('gotA',time.ctime())
		Lock.release()
		Lock.release()
	
	def run():
		self.doA()
		self.doB()
	
if __name__ == '__main__':
	
	#LockA = threading.Lock()
	#LockB = threading.Lock()
	
	#多重锁,不同函数的限制不同但互相调用造成.根本无法避免

	Lock = threading.RLock()	#递归锁,可重用的锁.通过内部对计时器的加减操作防止死锁
	threads = []
	for i in range(5):
		threads.append(MyThread())
	for t in threads:
		t.start()
	for t in threads:
		t.join()
'''

'''
#信号量Semaphore锁
#用来控制线程并发数
#BoundedSemaphore将调用release()时检查计数器,如果超过将抛出错误,
#	Semaphore不会抛出错误
import threading,time
class myThread(threading.Thread):
	def run(self):
		if semaphore.acquire():
			print(self.name)
			time.sleep(1)
			semaphore.release()

if __name__ == '__main__':
	semaphore = threading.Semaphore(5)
	thrs=[]
	for i in range(20):
		thrs.append(myThread())
	for t in thrs:
		t.start()
'''

'''
#条件变量Condition
#利用设置阻塞等实现线程间的通讯
import threading,time
from random import randint
class myThr(threading.Thread):
    def run(self):
    	global l
		while True:
    		val = randint(0, 100)
			print(self.name,'Append'+str(val), l)
			if lock_con.acquire():
				l.append(val)
				lock_con.notify()	#条件创造后调用,通知等待池激活一个线程
				#lock_con.notifyAll()	#条件创造后调用,通知等待池激活所有线程
				lock_con.release()
			time.sleep(2)

class Consumer(threading.Thread):
    def run(self):
    	global l
		while True:
    		lock_con.acquire()
			if len(l)==0:
    			lock_con.wait()	#条件不满足时调用,线程释放锁进入等待阻塞,之后再次跳转到acquire处
			print(self.name,'Delate'+str(l[0]),l)
			del l[0]
			lock_con.release()
			time.sleep(0.25)

if __name__ == '__main__':
    l = []
	lock_con = threading.Condition()	#创建条件变量锁
	threads=[]
	for i in range(5):
    	threads.append(myThr())
	threads.append(Consumer())
	for t in threads:
    	t.start()
	for t in threads:
    	t.join()
'''

'''
#同步事件Event,不是锁
#和条件变量相似,但少了锁的功能
import threading,time
class Boss(threading.Thread):
    def run(self):
    	print('jiaban')
		event.isSet() or event.set()	#isSet()返回状态值,set()将状态值设为True
		time.sleep(2)
		print('xiaban')
		event.isSet() or event.set()

class Worker(threading.Thread):
    def run(self):
    	event.wait()	#状态值为False时线程阻塞,为True时继续线程
		print('see')
		time.sleep(0.25)
		event.clear()	#将状态值设为False
		event.wait()
		print('xiaban')

if __name__ =='__main__':
    event = threading.Event()	#创建同步事件
	threads = []
	for i in range(5):
		threads.append(Worker())
	threads.append(Boss())
	for t in threads:
    	t.start()
	for i in threads:
    	i.join()
'''

'''
#队列
#FIFO先进先出,线程安全
import queue

d = queue.Queue(5)      #创建最长为 5 的队列,默认无限大队列

d.put('str')     #压入数据
d.put('int')
d.put('char')
##d.put('s',0) 超出最大长时,程序将阻塞 等待弹出.1为阻塞,0为抛错

d.get()     #弹出数据
##d.get(0)   超出存在长度时,程序也将阻塞 等待压入.1为阻塞,0为抛错

d.qsize()	#返回队列大小

d.full()	#满队列则返回True
d.empty()	#空队列则返回True
'''