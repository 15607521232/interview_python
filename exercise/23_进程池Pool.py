#coding=utf-8

from multiprocessing import Pool,Process
import time,os,random

def worker(msg):
    t_start = time.time()
    print("%s开始执行，进程号为%d" %(msg,os.getpid()))
    random.random()
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,"执行完毕，耗时%0.2f" %(t_stop-t_start))

if __name__ == '__main__':
    p = Pool(3)
    for i in range(10):
        #每次循环将会使用空闲出来的子进程去调用目标
        p.apply_async(worker,(i,))
    print('--start---')
    #关闭进程池
    p.close()
    #等待p中所有的子进程执行结束，必须在close语句之后
    p.join()
    print('--end--')