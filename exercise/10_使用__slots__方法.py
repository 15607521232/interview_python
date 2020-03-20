#coding=utf-8


'''如果我们想要限制实例的属性怎么办？比如，只允许对 Student
实例添加 name 和 age 属性'''


class Student():
    __slots__ = ('name','age') #用元组tuple定义允许绑定的属性名称

s = Student()
s.name = "liguang"
s.age = "25"


print(s.name  + " && " + s.age)


'''
1:定义一个特殊的 __slots__ 变量，来限制该 class 实例能添加的属性
2:使用 __slots__ 要注意， __slots__ 定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：


Traceback (most recent call last):
  File "E:/pythonWorkspace/interview_python/exercise/10_使用__slots__方法.py", line 19, in <module>
    s.score = 100
AttributeError: 'Student' object has no attribute 'score
'''

# s.score = 100
# print(s.score)

class GraduateStudent(Student):
    pass

gs = GraduateStudent()
gs.score = 99
print(gs.score)

