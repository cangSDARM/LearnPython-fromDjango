#多进程
#多进程数据是完全独立的
#和多线程相似,可以用函数或类的继承来创建(mthreading.py)
from multiprocessing import Process,Queue,Pipe     #多进程模块
import os
import time

def info(n, q):     #通讯需要传入q
    time.sleep(1)
    print('hallo', str(n))
    print('module',__name__)
    print('parent process',os.getppid())    #父进程pid
    print('process id',os.getpid())     #子进程pid
    q.put([n, 'hallo'])
    
#通过Queue来实现进程通信
def QueueCommunication():
    q = Queue()     #创建进程队列,实现进程之间的通信
    pL =[]

    #info('\033[32;1m main process line\033[0m')
    #time.sleep(2)

    for i in range(3):
        p = Process(target=info, args=(i, q))  #创建多进程
        p.start()      #开始子进程
        pL.append(p)

    print(q.get())      #子进程和主进程的queue是完全拷贝,不同的queue
    print(q.get())      #进程之间的queue通过pickle来通信
    print(q.get())

    for p in pL:
        p.join()    #多进程必须join,否则会成为僵尸进程,抢占系统资源

    print('end')

#通过pipe实现通信
def PipeCommuncation(conn):
    conn.send([42, None, 'hello'])  #管道send是str,不用转为bytes
    conn.close()    #关闭管道,但不会关闭子进程

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()    #创建管道,实现进程之间的通信.管道类似于socket,用send和recv实现通信
    p = Process(target=PipeCommuncation, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()
