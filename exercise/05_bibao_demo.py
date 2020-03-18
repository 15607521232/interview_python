#coding=utf-8

def line(k,b):
    print(id(line))
    def creat_y(x):
        print(id(creat_y))
        print(k * x  + b)
    return creat_y

line_1 = line(2,3)
print(id(line_1))
print(id(line))
line_1(3)


x = 300
def test1():
    x = 200
    def test2():
        nonlocal x
        print("---1-----x=%s" % x)
        x = 100
        print("---1-----x=%s" % x)
    return test2

res = test1()
res()