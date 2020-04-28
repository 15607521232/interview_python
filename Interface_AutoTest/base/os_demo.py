#coding=utf-8


import os,sys
def run():
    # os.system("ipconfig")
    p = os.popen("ipconfig")
    print(p.read())

def sort_list():
    d = {"a":24,"m":52,"i":12,"k":33}
    print(d.items())
    d1= sorted(d.items(),key=lambda x: x[1])
    print(d1)
    d2 = sorted(d.items(),key=lambda x: x[0])
    print(d2)

# f = lambda a,b: a+b
# f(20,30)


def main():
    # run()
    sort_list()

if __name__ == "__main__":
    main()