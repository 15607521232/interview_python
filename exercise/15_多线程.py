#coding=utf-8

import  threading

from time import ctime,sleep

def sing():
    for i in range(5):
        print("正在唱唱歌 %d" % i)
        sleep(1)

def dance():
    for i in range(5):
        print("正在跳舞 %d" % i)
        sleep(1)



if __name__ == '__main__':
    print('---开始----:%s' %ctime())
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    t1.start()
    t2.start()

    while True:

        #查看线程数量使用函数enumerate
        length = len(threading.enumerate())
        print('当前运行的线程数为%s' % length)
        if length<=1:
            break
        sleep(0.5)

    print('---结束----:%s' % ctime())
