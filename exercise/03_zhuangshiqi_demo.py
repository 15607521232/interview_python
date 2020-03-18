#coding=utf-8
import time

# def new_demo():
#     print(time.localtime())
#
# f = new_demo
# f()
# print(type(f))
# print(f.__name__)
# print(new_demo.__name__)
#装饰器decorator本质上就是一个返回函数的高阶函数
# def log(func):
#     def wrapper(*args,**kwargs):
#         print('call %s():' % func.__name__)
#         return func(*args,**kwargs)
#     return wrapper
#
# @log
# def now():
#     print("2020-3-18")
#
# now()

#
# def display_time(func):
#     def wrapper():
#         t1 = time.time()
#         func()
#         t2 = time.time()
#         print(t2 - t1)
#     return wrapper
#
#
# def is_prime(num):
#     if num < 2:
#         return False
#     elif num ==2:
#         return True
#     else:
#         for i in range (2,num):
#             if num % i == 0:
#                 return False
#         return True
#
# @display_time
# def prime_nums():
#     my_list = []
#     for i in range(2,10000):
#         if is_prime(i):
#             my_list.append(i)
#     print(my_list)
#
#
# prime_nums()


def set_func(func):
    print("set_func:%s" %(id(set_func)))
    def call_func():
        print("call_func:%s" % (id(call_func)))
        print("---这是权限验证1---")
        print("---这是权限验证2---")
        func()
        print("func:%s" %(id(func)))
    return call_func

@set_func #等价于ret = set_func(test1)
def test1():
    print("test1:%s" % (id(test1)))
    print("---test1---")

test1()

#这是装饰器的分解步骤
'''
1:将set_func()函数赋值给test1,ret指向call_func,func指向函数test1
2:执行test1(),相当于额执行call_func()
3:执行call_func()
'''

#先执行等号右边的set_func(test1)
# test1 = set_func(test1)
# test1()
