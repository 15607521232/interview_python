#coding=utf-8


'''
当我们需要定义常量时，一个办法是用大写变量通过整数来定义,
更好的方法是为这样的枚举类型定义一个 class 类型，然后，每个常量
都是 class 的一个唯一实例。Python 提供了 Enum 类来实现这个功能


既可以用成员名称引用枚举常量，又可以直接根据 value 的值获
得枚举常量
'''

from enum import Enum,unique

Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))

for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)

@unique
class Weekday(Enum):
    sun = 0
    mon = 1
    tue = 2
    wed = 3
    thu = 4
    fri = 5
    sat = 6

day1 = Weekday.mon
print(day1)

print(Weekday.thu.value)