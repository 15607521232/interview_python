#coding=utf-8

'''

type() 函数可以查看一个类型或变量的类型
 Hello 是一个 class，它的类型就是 type ，而 h 是一个实例，它的类型就是 class  Hello

 type() 函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过 type() 函数创建出 Hello 类，而无需通过 classHello(object)... 的定义
'''

class Hello():
    def hello(self,name='world'):
        print('Hello, %s' % name)

h = Hello()
h.hello()

print(type(Hello)) #<class 'type'>
print(type(h)) #<class '__main__.Hello'>

print("*" * 50)

'''
要创建一个 class 对象， type() 函数依次传入 3 个参数：
1. class 的名称；
2. 继承的父类集合，注意 Python 支持多重继承，如果只有一个父类，
别忘了 tuple 的单元素写法；
3. class 的方法名称与函数绑定，这里我们把函数 fn 绑定到方法名
hello 上。
'''


def fn(self,name="world"):
    print('Hello %s' %name)
Hello_Type = type('Hello_Type',(object,),dict(hello=fn))

ht = Hello_Type()
ht.hello()


'''
元类
除了使用 type() 动态创建类以外，要控制类的创建行为，还可以使用
metaclass。
metaclass，直译为元类
metaclass 是类的模板，所以必须从`type`类型派生
__new__() 方法接收到的参数依次是：
1. 当前准备创建的类的对象；
2. 类的名字；
3. 类继承的父类集合；
4. 类的方法集合
'''


class ListMetaClass(type):
    def __new__(cls, name,bases,attrs):
        attrs['add'] = lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)

class MyList(list,metaclass=ListMetaClass):
    pass


l = MyList()
l.add(1)
print(l)

