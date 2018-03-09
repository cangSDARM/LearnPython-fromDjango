#进程池和进程管理
from multiprocessing import Process, Manager

def f(d, l, n):
    d[n] = '1'
    l.append(n)

if __name__ == "__main__":
    with Manager() as manager:    #实现数据共享
        d = manager.dict()      #进程之间可以共享
        l = manager.list(range(5))  #进程之间可以共享
        pL = []

        for i in range(10):
            p = Process(target=f, args=(d, l, i))
            p.start()
            pL.append(p)

        for res in pL:
            res.join()

        print('d:',d)
        print('l:',l)