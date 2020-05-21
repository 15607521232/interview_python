#coding=utf-8


def f(x,l=[]):
    for i in range(x):
        l.append(i * i)
    print(l)

if __name__ == '__main__':
    # f(2)
    # f(3,[3,2,1])
    f(3)

#2020-05-20T10:42:50.935748Z 1 [Note] A temporary password is generated for root@localhost: -duU5uEapgqf

#mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY '930819@LiGuang';

 #grant all privileges on *.* to root@'%'identified by '930819@LiGuang';