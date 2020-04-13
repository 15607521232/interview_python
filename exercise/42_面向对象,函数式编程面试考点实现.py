#coding=utf-8

#用函数方法实现计算集合 list1 = [1,2,3,4,5]中，所有元素的和

list1 = [1,2,3,4,5]
def list_sum(list):
    x = 0
    for i in list1:
        x += i
    return x

li_sum = list_sum(list1)
print(li_sum)