#coding=utf-8


class Student():

    def get_score(self):
        return self.__score


    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError ("成绩必须是整数")
        elif value <0 or value >100:
            raise ValueError("成绩不符合要求")
        else:
            self.__score = value

s = Student()
'''
Traceback (most recent call last):
  File "E:/pythonWorkspace/interview_python/exercise/11_使用property装饰器.py", line 19, in <module>
    s.set_score(101)
  File "E:/pythonWorkspace/interview_python/exercise/11_使用property装饰器.py", line 14, in set_score
    raise ValueError("成绩不符合要求")
ValueError: 成绩不符合要求
'''

s.set_score(10)
s_score = s.get_score()
print(s_score)


class GraduateStudent():
    @property
    def score(self):
        return self.__score


    @score.setter
    def score(self,value):
        if not isinstance(value, int):
            raise ValueError("成绩必须是整数")
        elif value < 0 or value > 100:
            raise ValueError("成绩不符合要求")
        else:
            self.__score = value
'''@property 的实现比较复杂，我们先考察如何使用。把一个 getter 方法变
成属性，只需要加上 @property 就可以了，此时， @property 本身又创建
了另一个装饰器 @score.setter ，负责把一个 setter 方法变成属性赋值'''

gs = GraduateStudent()
gs.score = 166
print(gs.score)
