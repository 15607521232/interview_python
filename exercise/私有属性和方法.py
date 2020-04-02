#coding=utf-8

_num = 1
num = 11


class Person():
    def __init__(self,name,age,hobby):
        self.name = name
        self._age = age
        self.__hobby = hobby

    def show_person(self):
        print(self.name)
        print(self._age)
        print(self.__hobby)

class Student(Person):
    def construction(self,name,age,hobby):
        self.name = name
        self._age = age
        self.__hobby = hobby
    def show_student(self):
        print(self.name)
        print(self._age)
        print(self.__hobby)

# s1 = Student('su',25,'baseball')
# # s1.show_student()
# s1.show_person()
# print("*" * 20)
# s1.construction('li',30,'cook')
# s1.show_person()
# print("*" * 20)
# s1.show_student()

# def test():
#     print("---test----")





