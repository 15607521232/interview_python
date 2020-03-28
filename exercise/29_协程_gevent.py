#coding=utf-8

from gevent import monkey
import gevent
import random
import time


#将程序中用到的耗时操作的代码，换为gevent中自己实现的模块
monkey.patch_all()


def test(a):
    for i in range(10):
        print(a,i)
        time.sleep(random.random())

gevent.joinall([
    gevent.spawn(test,"test1"),
    gevent.spawn(test,"test2")
])