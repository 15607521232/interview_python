#coding=utf-8

def test_arg1(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


def test_arg(a,b,name="liguang",*args,**kwargs):
    print(a)
    print(b)
    print(name)
    print(args)
    print(kwargs)
    test_arg1(a,b,name="huang",*args,**kwargs)

test_arg(110,100,"subiao","hanhaodong",sex="boy")
print("*" *  50)
test_arg(b=20,a=10)
print("*" * 50)

temp = ("su","chen","wang")
kw_temp = {"gender":True,"hobby":"baseball"}
test_arg(11,20,temp,kw_temp)
print("*" * 50)
test_arg(11,20,*temp,**kw_temp)
print("*" * 50)

test_arg(11,22,33,44,55,66,sex="boy")