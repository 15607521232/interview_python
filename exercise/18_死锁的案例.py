#coding=utf-8

import threading
import time


mutexA = threading.Lock()
mutexB = threading.Lock()

class MyThreadA(threading.Thread):
    def run(self) -> None:
        mutexA.acquire()

        #mutexA上锁后，延时一秒，等待另外那个线程，把mutexB上锁
        print(self.name + '---do1---up----')
        time.sleep(1)

        #此时会堵塞，因为这个mutexB已经被另外的线程抢先上锁了
        mutexB.acquire()
        print(self.name + '---do1---down----')
        mutexB.release()


        #解锁mutexA
        mutexA.release()

class MyThreadB(threading.Thread):
    def run(self) -> None:
        mutexB.acquire()

        # mutexB上锁后，延时一秒，等待另外那个线程，把mutexA上锁
        print(self.name + '---do2---up')
        time.sleep(1)

        mutexA.acquire()
        print(self.name + '---do2---down----')
        mutexA.release()

        mutexB.release()

if __name__ == '__main__':
    t1 = MyThreadA()
    t2 = MyThreadB()

    t1.start()
    t2.start()