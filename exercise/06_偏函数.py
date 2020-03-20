#coding=utf-8

import functools


'''
当函数的参数个数太多，需要简化时，使用 functools.partial 可以创建一个新的函数， ，从而在调用时更简单
'''

int2 = functools.partial(int,base=2)
print(int2('100'))


