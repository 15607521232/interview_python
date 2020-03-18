#coding=utf-8

#对有参数，没返回值的函数进行装饰

def set_func(func):
    def call_func(num):
        print("---这是装饰器---")
        print("---这是装饰器---")
        func(num)
    return call_func


@set_func
def set_num(num):
    print("----num:%d----" % num)

set_num(100)
