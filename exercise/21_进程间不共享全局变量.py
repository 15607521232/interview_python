#coding=utf-8

from multiprocessing import Process
import os
from time import sleep

nums = [11,22,33]

def work1():
    print('in process1 pid=%d' % os.getpid(),nums)
    for i in range(3):
        nums.append(i)
        sleep(1)
        print('in process1 pid=%d,nums=%s' %(os.getpid(),nums))

def work2():
    print('in process2 pid=%d' % os.getpid(), nums)


if __name__ == '__main__':
    p1 = Process(target=work1)
    p1.start()
    p1.join()


    p2 = Process(target=work2)
    p2.start()

'''
in process1 pid=21896 [11, 22, 33]
in process1 pid=21896,nums=[11, 22, 33, 0]
in process1 pid=21896,nums=[11, 22, 33, 0, 1]
in process1 pid=21896,nums=[11, 22, 33, 0, 1, 2]
in process2 pid=16344 [11, 22, 33]
'''