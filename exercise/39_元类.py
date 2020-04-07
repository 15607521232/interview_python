#coding=utf8


class Test():
    #类属性
    num = 0
    names = ['li','su']
#使用type创建类
Test2 = type("Test2",(),{"gender":"1000"})

print(Test.num)
#添加类属性
Test.sex = "boy"
print(Test.__dict__)
print(Test.__class__)
print("*" * 50)
print(Test2)
t2 = Test2()
print(t2.gender)

#使用type创建继承类
Test2Child = type("Test2Child",(Test2,),{"gender2":"2000"})
t2c = Test2Child()
print(t2c.gender)