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
def log(func):
    def wrapper(*args,**kwargs):
        print('call %s():' % func.__name__)
        return func(*args,**kwargs)
    return wrapper

@log
def now():
    print("2020-3-18")

now()
