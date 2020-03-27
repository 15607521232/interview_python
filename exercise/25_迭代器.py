#coding=utf-8

from collections import Iterable
class MyList():

    '''自定义一个可迭代对象'''
    def __init__(self):
        self.container = []
    def add(self,item):
        self.container.append(item)
    def __iter__(self):
        myiterator = MyIterator(self)
        return myiterator

class MyIterator():
    '''自定义一个供上面的迭代对象使用的迭代器'''
    def __init__(self,mylist):
        self.mylist = mylist
        self.current = 0
    def __next__(self):
        if self.current<len(self.mylist.container):
            item = self.mylist.container[self.current]
            self.current += 1
            return item
        else:
            raise StopIteration

    def __iter__(self):
        return self

mylist = MyList()
mylist.add(1)
mylist.add(2)
mylist.add(3)

print(isinstance(mylist,Iterable))

for i in mylist:
    print(i)
