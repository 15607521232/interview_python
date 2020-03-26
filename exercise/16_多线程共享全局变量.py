#coding=utf-8


import threading
from time import ctime,sleep

# class MyThread(threading.Thread):
#
#     def run(self):
#         for i in range(3):
#             sleep(1)
#             msg = "我是" + self.name  + "@" + str(i)
#             print(msg)
#
# if __name__ == '__main__':
#     t = MyThread()
#     t.start()

'''
在一个进程内的所有线程共享全局变量，很方便在多个线程间共享数据
缺点就是，线程是对全局变量随意遂改可能造成多线程之间对全局变量的混乱（即线程非安全）
'''

g_num = 100
g_nums = [11,22,33]
def work1(num_list):
    num_list.append(44)
    global g_num
    for i in range(3):
        g_num += 1
    print("in work1 g_num %d" % g_num)
    print("in work1 num_list", num_list)

def work2(num_list):
    global g_num
    print("in work2 g_num %d" % g_num)
    print("in work2 num_list", num_list)

if __name__ == '__main__':
    print("线程创建之前的g_num 是 %d" % g_num)

    t1 = threading.Thread(target=work1,args=(g_nums,))
    t2 = threading.Thread(target=work2,args=(g_nums,))

    t1.start()
    sleep(2)
    t2.start()