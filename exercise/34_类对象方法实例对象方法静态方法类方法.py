#coding=utf-8

class Man():
    #类属性
    gender = "boy"

    def __init__(self,name):

        #实例属性
        self.name = name


    def run(self):
        print(self.name + " is running")

    @classmethod
    def cls_eat(cls):
        """ 定义类方法，至少有一个cls参数 """
        print("the man is eating")


    @staticmethod
    def sta_drink():
        """ 定义静态方法 ，无默认参数"""
        print("the man is drinking")

#创建实例对象
li = Man("liguasng")
#调用类属性
print(li.gender)
#调用实例方法
li.run()
#调用类方法
li.cls_eat()
#调用静态方法
li.sta_drink()