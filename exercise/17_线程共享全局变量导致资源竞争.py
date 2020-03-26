#coding=utf-8

import threading
from time import ctime,sleep

'''如果多个线程同时对同一个全局变量操作，会出现资源竞争问题，从而数据结果会不正确
解决方法：可以使用线程同步的方式来解决
思路，如下:
系统调用t1，然后获取到g_num的值为0，此时上一把锁，即不允许其他线程操作g_num
t1对g_num的值进行+1
t1解锁，此时g_num的值为1，其他的线程就可以使用g_num了，而且是g_num的值不是0而是1
同理其他线程在对g_num进行修改时，都要先上锁，处理完后再解锁，在上锁的整个过程中不允许其他线程访问，就保证了数据的正确性

线程同步能够保证多个线程安全访问竞争资源，最简单的同步机制是引入互斥锁。
互斥锁为资源引入一个状态：锁定/非锁定
某个线程要更改共享数据时，先将其锁定，此时资源的状态为“锁定”，其他线程不能更改；直到该线程释放资源，将资源的状态变成“非锁定”，其他的线程才能再次锁定该资源。互斥锁保证了每次只有一个线程进行写入操作，从而保证了多线程情况下数据的正确性。
'''


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
    t1 = threading.Thread(target=work1,args=(100000,))
    t2 = threading.Thread(target=work2,args=(100000,))
    t1.start()
    t2.start()

    while len(threading.enumerate()) != 1:
        sleep(1)
    print("两个线程对同一个变量操作的最终结果:%s" % g_num)


#解决方法
'''
num =0
#创建锁
mutex = threading.Lock()


def test1(n):
    global num

    #上锁
    mutex.acquire()
    for i in range(n):
        num +=1

    #解锁
    mutex.release()
    print('--in test1 num=%d' %num)

def test2(n):
    global num

    mutex.acquire()
    for i in range(n):
        num += 1
    mutex.release()
    print('--in test2 num=%d' %num)

def main():
    t1 = threading.Thread(target=test1,args=(1000000,))
    t2 = threading.Thread(target=test2,args=(1000000,))

    t1.start()
    t2.start()
    time.sleep(2)
    print("---in main thread---num=%d" %num)

if __name__ == '__main__':
    main()
'''
