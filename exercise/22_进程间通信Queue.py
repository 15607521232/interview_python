#coding=utf-8

from multiprocessing import Process,Queue
import os,time,random

def write(q):
    for value in ['A','B','C']:
        print('put %s to queue' %value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print('Get %s from Queue' %value)
            time.sleep(random.random())
        else:
            break

if __name__ == '__main__':
    #父进程创建Queue，并传递给各个子进程
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))

    #启动pw写入
    pw.start()

    #等待
    pw.join()

    #启动pr读取
    pr.start()
    pr.join()

    #pr里是死循环，无法等待结束，强行终止
    # print('所有数据已写读结束')


