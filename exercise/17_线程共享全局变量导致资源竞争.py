#coding=utf-8

import threading
from time import ctime,sleep

'''如果多个线程同时对同一个全局变量操作，会出现资源竞争问题，从而数据结果会不正确'''
g_num = 0
def work1(num):
    global g_num
    for i in range(num):
        g_num  += num
        print("in work1 g_num %d" % g_num )
def work2(num):
    global g_num
    for i in range(num):
        g_num += num
        print("in work2 g_num %d" % g_num)

if __name__ == '__main__':
    t1 = threading.Thread(target=work1,args=(10000000,))
    t2 = threading.Thread(target=work2,args=(10000000,))
    t1.start()
    t2.start()

    while len(threading.enumerate()) != 1:
        sleep(1)
    print("两个线程对同一个变量操作的最终结果:%s" % g_num)
