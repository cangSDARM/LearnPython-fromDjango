#并发多线程, IO密集型
#计算密集型, 改C语言

'''通过函数创建进程
import threading
import time
	
def foo(n):
    for i in range(2):
		print('foo%s'%n)
        time.sleep(2)
	
def bar(n):
    for i in range(2):
        print('bar%s'%n)
        time.sleep(1)
	
#创建线程对象
t1 = threading.Thread(target=foo, args=(3,))
t2 = threading.Thread(target=bar, args=(2,))
threads = []
threads.append(t1)
threads.append(t2)
	
if __name__ == '__main__':
    t2.setDaemon(True)   #守护线程, 主线程结束后,t2子线程强制结束
    for t in threads:
        t.start()  #开启线程
    
    t.join()   #t2线程不结束不执行之后代码
    
    print('end of all')
'''

'''通过类创建进程
import threading
import time
	
class MyThread(threading.Thread):
	def __init__(self, num):
		threading.Thread.__init__(self)
		self.num = num
	
	def run(self):	#定义每个线程要运行的函数
		print('running:%s'%self.num)
	
if __name__ == '__main__':
	t1 = MyThread(1)
	t2 = MyThread(2)
	t1.start()
	t2.start()
'''

'''同步锁,防止多线程在操作相同变量时调用顺序出错
import threading
import time
	
def subnum():
	global num
	r.acquire()		#调用同步锁,防止CPU自动切换线程
	temp = num
	time.sleep(1)
	num = temp - 1
	r.release()		#释放同步锁
	
num = 20
	
r = threading.Lock()	#申请同步锁
if __name__ == '__main__':
	for i in range(20):
		t = threading.Thread(target=subnum)
		t.start()
'''

#GIL全局解释器锁(解释器Cpython). 在同一时刻只能有一个线程进入解释器,使得python无法使用"并行多线程",需要通过"多进程"解决
'''
'''
