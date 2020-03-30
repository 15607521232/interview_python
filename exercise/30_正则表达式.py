#coding=utf-8


import re

result = re.match("itcast","itcast.cn")
ret = re.match(".","M")

ret1 = re.match("[hH]ello","Hello Python")
ret2 = re.match("[0-9]Hello python","8Hello python")

with open("a.txt","r") as file:
    file_re = file.read()
ret3 = re.match("嫦娥\d号",file_re)
ret4 = re.match("[1-9]?\d$|100","80")
ret5 = re.match("\w{4,20}@(163|126|qq)\.com","test@163.com")
print(result.group())
print(ret.group())
print(ret1.group())
print(ret2.group())
print(ret3.group())
print(ret4.group())
print(ret5.group())
print("*" * 50)
#search
ret6 = re.search(r"\d+","阅读次数889")
print(ret6.group())
print("*" * 50)
#findall 不能用ret7.group()
ret7 = re.findall(r"\d+","python=1000, c=2000, c++=3000")

print(ret7)

#sub,将匹配到的结果替换
ret8 = re.sub(r"\d+",'1000',"python=500")
print("*" * 50)
print(ret8)
