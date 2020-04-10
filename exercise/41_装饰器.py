#coding=utf-8
import time

#请实现:@runtime 效果为当前调用studennt_run时会自动打印当前时间

def runtime(func):
    def get_nowtime(*args):
        print(time.ctime())
        func(*args)
    return get_nowtime




@runtime
def student_run(name):
    print("student" + name + "run")



student_run("张三")


#请简述func1 和func2函数的返回值，以及函数的运行机制

def func1():
    for i in range(1,5):
        return i

def func2():
    for i in range(1,5):
        yield i

f1 = func1()
print(f1)
f2 = func2()
print(f2)
for i in f2:
    print(i)