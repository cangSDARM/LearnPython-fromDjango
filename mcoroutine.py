#协程Coroutine
#   本质是单线程
#优点
#   无须CPU切换开销
#   没有锁定和同步开销
#   方便切换控制流,适合高并发
#缺点
#   进行阻塞会阻塞整个程序
#   无法利用多核CPU

'''
#yield支持的协程,最底层通过生成器迭代
import time
import queue

def consumer(name):
    print('*'*10)
    while True:
        next_d = yield      #有yield就是生成器,且返回值为 yield+返回值
        print('[%s] doe %s'%(name, next_d))

def producter():
    con.__next__()  #同下
    next(con2)      #next反复调用生成器,直到协程里没有yield
    n = 0
    while n<5:
        n +=1
        print('\033[32;1m[producter]\033[0m is making %s'%n)
        con.send(n)     #传值给生成器,第一次传递时,send不能有值
        con2.send(n)


if __name__ == '__main__':
    con = consumer('c1')    #创建一个生成器对象
    con2 = consumer('c2')
    producter()
'''

'''
#greenlet的协程
import greenlet
def f():
    print(12)
    gr2.switch()        #switch类似于yield,直接切换到gr2
    print(34)
    gr2.switch()

def d():
    print(56)
    gr1.switch()
    print(78)

gr1 = greenlet.greenlet(f)  #创建greenlet对象
gr2 = greenlet.greenlet(d)
gr1.switch()
'''

'''
#gevent的协程,爬虫初步
from gevent improt monkey
monkey.patch_all()      #加速IO阻塞监听,提高切换速度
import gevent
from urllib.request import urlopen

def f(url):
    print('get:%s'%url)
    resp = urlopen(url)
    data = resp.read()      #IO阻塞,gevent遇见则自动切换
    print('%d bytes recevied'%len(data))

gevent.joinall(     #连接方法
    [
        gevent.spawn(f, 'https://www.python.org/'),      #激活函数,同时激活
        gevent.spawn(f, 'https://www.baidu.com/'),
        gevent.spawn(f, 'https://github.com/'),
    ]
)
'''


