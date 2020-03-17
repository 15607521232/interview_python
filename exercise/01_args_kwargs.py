#coding=utf-8

my_list = ["aaaaaaaaa","bbbbb","cccccc"]

def run(*args):
    for count,thing in enumerate(args):
        print("{0} , {1}".format(count,thing))


def table_thing(**kwargs):
    print(kwargs.items())
    for name,value in kwargs.items():
        #items  返回可遍历的（键,值）元组数组
        print("{0} = {1}".format(name,value))


def print_three_thing(a,b,c):
    print("a={0},b={1},c={2}".format(a,b,c))

if __name__ == '__main__':
    run("apple","banana","tomato")
    print("------" * 10)
    table_thing(apple="fruit",su="li")
    print("------" * 10)
    print_three_thing(*my_list)
