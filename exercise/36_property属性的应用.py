#coding=utf-8


class Money():
    def __init__(self):
        self.__money = 100

    def getMoney(self):
        return self.__money

    def setMoney(self,value):
        if isinstance(value,int):
            self.__money =value
        else:
            print("数值类型错误")

    def delMoney(self):
        del self.__money

    money = property(getMoney,setMoney,delMoney,"设置私有属性")

m = Money()
print(m.money)
m.money = 200
print(m.money)
print(Money.money.__doc__)
print("*" * 50)



class Money_Pro():
    def __init__(self):
        self.__money = 120

    @property
    def money(self):
        return self.__money


    @money.setter
    def money(self,value):
        if isinstance(value,int):
            self.__money = value
        else:
            print("数值类型错误")

mp = Money_Pro()
print(mp.money)
mp.money = 300
print(mp.money)