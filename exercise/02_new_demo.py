#coding=utf-8

class Singleton():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,"-instance"):
            orig = super(Singleton,cls)
            cls._instance = orig.__new__(cls,*args,**kwargs)
            return cls._instance
class MyClass(Singleton):
    a = 1

mc = MyClass()
print(mc)
print(mc.a)
