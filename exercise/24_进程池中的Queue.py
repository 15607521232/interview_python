#coding=utf-8

from multiprocessing import Pool,Queue,Process,Manager
import time,os,random

def reader(q):
    print("reader启动(%s),父进程为(%s)" %(os.getpid(),os.getppid()))
    for i in range(q.qsize()):
        print("reader从queue中获取到消息:%s" % q.get(True))


def writer(q):
    print("writer启动(%s)，父进程为(%s)" %(os.getpid(),os.getppid()))
    for i in "hello python":
        q.put(i)



if __name__ == '__main__':
    print("(%s)start" %(os.getpid()))
    q = Manager().Queue()
    p = Pool()
    p.apply_async(writer,(q,))

    time.sleep(1)

    p.apply_async(reader,(q,))
    p.close()
    p.join()
    print("(%s) end" %(os.getpid()))
'''
(14528)start
writer启动(15764)，父进程为(14528)
reader启动(6484),父进程为(14528)
reader从queue中获取到消息:h
reader从queue中获取到消息:e
reader从queue中获取到消息:l
reader从queue中获取到消息:l
reader从queue中获取到消息:o
reader从queue中获取到消息: 
reader从queue中获取到消息:p
reader从queue中获取到消息:y
reader从queue中获取到消息:t
reader从queue中获取到消息:h
reader从queue中获取到消息:o
reader从queue中获取到消息:n
(14528) end

'''