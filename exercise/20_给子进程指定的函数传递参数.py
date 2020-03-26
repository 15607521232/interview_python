#coding=utf-8

from multiprocessing import Process
import time
import os

def run_proc(name,age,**kwargs):
    for i in range(10):
        print('子进程运行中，name=%s,age=%d,pid=%d...' %(name,age,os.getpid()))
        print(kwargs)
        time.sleep(0.2)

if __name__ == '__main__':
    p = Process(target=run_proc,args=('test',18),kwargs={"m":20})
    p.start()
    time.sleep(1)
    #管任务是否完成，立即终止子进程
    p.terminate()
    #是否等待子进程执行结束，或等待多少秒
    p.join()

'''
子进程运行中，name=test,age=18,pid=47768...
{'m': 20}
子进程运行中，name=test,age=18,pid=47768...
{'m': 20}
子进程运行中，name=test,age=18,pid=47768...
{'m': 20}
子进程运行中，name=test,age=18,pid=47768...
{'m': 20}

'''