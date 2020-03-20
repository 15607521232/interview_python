#coding=utf-8

class Student():
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return 'Student object(name:%s)' % self.name

    __repr__ = __str__
s = Student("liguang")  # 不定义__str__,打印<__main__.Student object at 0x0000026C8CB45D30>，定义__str__,打印Student object(name:liguang)
print(s)


'''
如果一个类想被用于 for ... in 循环，类似 list 或 tuple 那样，就必须实
现一个 __iter__() 方法，该方法返回一个迭代对象，然后，Python 的 for
循环就会不断调用该迭代对象的 __next__() 方法拿到循环的下一个值，
直到遇到 StopIteration 错误时退出循环
'''

class Fib():
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a
my_list = []
for n in Fib():
    my_list.append(n)
print(my_list)


'''
Fib 实例虽然能作用于 for 循环，看起来和 list 有点像，但是，把它当成
list 来使用还是不行,要表现得像 list 那样按照下标取出元素，需要实现 __getitem__() 方法
'''

class Fib1():
    def __getitem__(self, n):
        a,b = 1,1
        for x in  range(n):
            a,b = b, a+b
        return a
f1 = Fib1()
print(f1[0])
print(f1[4])
print(f1[8])
print(f1[25])
print("*" * 10)
print(list(range(100))[5:10])


'''
正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错,要避免这个错误，除了可以加上一个 score 属性外，Python 还有另一个
机制，那就是写一个 __getattr__() 方法，动态返回一个属性,
也可以返回一个函数，只是调用方式要变成实例调用函数的方法
'''

class GetAttr():
    def __init__(self):
        self.name = "LiGuang"

    def __getattr__(self, item):
        if item == 'score':
            return 99
        if item == 'age':
            return lambda: 25
        raise AttributeError("\'GetAttr\' object has no attribute \'%s\'" % item)

ga = GetAttr()
print(ga.name)
print(ga.score)
print(ga.age())
'''
Traceback (most recent call last):
  File "E:/pythonWorkspace/interview_python/exercise/12_定制类.py", line 81, in <module>
    print(ga.abc)
  File "E:/pythonWorkspace/interview_python/exercise/12_定制类.py", line 75, in __getattr__
    raise AttributeError("\'GetAttr\' object has no attribute \'%s\'" % item)
AttributeError: 'GetAttr' object has no attribute 'abc'
'''
# print(ga.abc)

'''
1:任何类，只需要定义一个 __call__() 方法，就可以直接对实例进行调用
2:通过 callable() 函数，我们就可以判断一个对象是否是“可调用”对象
'''
class Call_Demo():
    def __init__(self,name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print('My name is %s. ' % self.name)

cd = Call_Demo('liguang')
cd()
print(callable(cd))


