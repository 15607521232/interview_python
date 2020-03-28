#coding=utf-8

from greenlet import greenlet
from time import sleep

def test1():
    while True:
        print('----A---')
        g2.switch()
        sleep(1)
def test2():
    while True:
        print('----B---')
        g1.switch()
        sleep(2)



if __name__ == '__main__':
    g1 = greenlet(test1)
    g2 = greenlet(test2)
    g1.switch()
