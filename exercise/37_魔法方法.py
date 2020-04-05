#coding=utf-8


'''
对象后面加括号，触发执行。
注：__init__方法的执行是由创建对象触发的，即：对象 = 类名()；而对于__call__方法的执行是由对象后加括号触发的，即：对象()或者类()()
'''

class Test():
    def __init__(self,name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print("__call__")

t = Test("test")
t()
