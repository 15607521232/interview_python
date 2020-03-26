#coding=utf-8

from multiprocessing import Process
import time
import os


def run():
    '''子进程要执行的代码'''
    print('子进程运行中，pid=%d' %os.getpid())
    print('子进程将要结束')

if __name__ == '__main__':
    print('父进程运行中，pid=%d' %os.getpid())
    p = Process(target=run)
    p.start()
