#coding=utf-8

'这是引用项目中的私有函数或者变量'

def _private_1(name):
    return "hello ,%s" % name

def __private_2(name):
    return "Hi %s" %name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return __private_2(name)