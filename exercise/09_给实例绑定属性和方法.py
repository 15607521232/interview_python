#coding=utf-8


from types import MethodType


class Student():
    pass


s = Student
s.name = 'li' #动态给实例绑定一个属性
print(s.name)

def set_age(self,age):
    self.age = age

s.set_age = MethodType(set_age,s)   #给实例绑定一个方法
s.set_age(25)
print(s.age)

s2 =Student()  #给一个实例绑定的方法，对另一个实例是不起作用的
print(s2.set_age(25))


def set_score(self,score):
    self.score = score

Student.set_score = MethodType(set_score,Student) #给 class 绑定方法,且所有实例都可以调用
s.set_score(100)
print(s.score)
s2.set_score(100)
print(s2.score)