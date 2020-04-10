#coding=utf-8
import copy

def test_num(temp):
    temp.append(33)

num_li = [11,22]
test_num(num_li)
print(num_li)
'''第一题'''

a = ('a','b','c')
c = copy.copy(a)
d = copy.deepcopy(a)

if c == d:
    print("c 和 d 相等")
if id(c) == id(d):
    print("c 和 d 地址相等")


'''第二题'''
class Person():
    x = 5
    y = 6
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y

person = Person(10,20)
person.z = 7
print(person.x)
print(person.y)
print(Person.x)
print(Person.y)
print(Person.add(Person))
print(person.add())
print(person.z)
# print(Person.z)

#python中一个函数function接收三个参数a,*args,**kwargs，他们分别是什么类型
#请根据列表list1 = [1,2,3,4,5,6],使用一行代码生成一个新的列表list2,list2中每个元素是list1的平方
list2 = [x * x for x in [1,2,3,4,5,6]]

list1 = [1,2,3,4,5,6]
result = map(lambda x: x * x,list1)
print(list(result))
print(result)
print(list2)
#请将下面的列表进行排序 list1 = [20,15,88,97,76,13,27,49]
list1 = [20,15,88,97,76,13,27,49]
ls = list1.sort(reverse=False)
print(ls)


#集合推导式
set1 = {1,2,3,4}
set2 = {i **3 for i in set1}
print(set2)


#字典推导式
my_json = {
    "key1":10,
    "key2":20,
    "key3":30,
}

keys = [key for key,value in my_json.items() ]
print(keys)

keys1 = {value:key for key,value in my_json.items()}
print(keys1)

keys2 = {key:value for key,value in my_json.items()  if value < 30}
print(keys2)