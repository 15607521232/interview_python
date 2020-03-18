#coding=utf-8

'''任何实现了__enter__()和__exit__()方法的对象都可称之为上下文管理器，上下文管理器对象可以使用with关键字。显然，文件（file）对象也实现了上下文管理器'''
class With_File():
    def __init__(self,filename,mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("entering")
        self.f = open(self.filename,self.mode)
        return self.f

    def __exit__(self,*args):
        print("will exit")
        self.f.close()

with With_File("a.txt","w") as f:
    print("writing")
    f.write("hello 上下文管理器 ")