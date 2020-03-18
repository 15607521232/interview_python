#coding=utf-8

#对有参数，没返回值的函数进行装饰

def set_func(func):
    def call_func(*args,**kwargs):
        print("---这是装饰器---")
        print("---这是装饰器---")
        # func(args,kwargs)  不行，相当于传递了两个参数，一个元组，一个字典
        return func(*args,**kwargs)  # *args和**kwargs相当于拆包
    return call_func


@set_func
def set_num(num,*args,**kwargs):
    print("----num:%d----" % num)
    print("args:",args)
    print("**kwargs:",kwargs)
    return "对带有返回值的函数进行装饰"

ret = set_num(100,200,300,400,mm=500)
print(ret)