#coding=utf-8


def fib(n):
    current = 0
    num1,num2 = 0,1
    while current < n:
        num = num1
        num1,num2 = num2,num1 + num2
        current +=1
        yield num
    return 'done'

f = fib(5)
while True:
    try:
        x = next(f)
        print("value:%d" %x)
    except StopIteration as e:
        print("生成器返回值:%s" % e.value)
        break

print("*" * 50)

def gen():
    i = 0
    while i < 5:
        temp = yield i
        print(temp)
        i+=1

g = gen()
print(next(g))
g.send("liguang")
print(next(g))
g.send("subiao")

