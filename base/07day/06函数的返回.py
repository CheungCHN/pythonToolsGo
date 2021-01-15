#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
#return表示函数执行完毕
def test01():
    s=10+20

    return s#return表示函数到这里就结束
    print(s)
test01()

def test02():
    return

print(test02())

def test03():
    return 10

print(test03())

def test04(a,b):
    return a+b

print(test04(10,20))

def test05(a):
    return a

print(test05(10))

def test06(a,b):
    return a>b

print(test06(10,20))

def test07(a,b):
    a=a+10
    b=b+10
    return a,b

a1,b1=test07(100,200)
print(a1,b1)

#案例:定义一个函数,这个函数返回多个值
def test08():
    return 10,20,30

x1,x2,x3=test08()
print(x1,x2,x3)


def test09(a,b):
    if a>b:
        return
    else:
        print(a,b)
    print("我想执行")


