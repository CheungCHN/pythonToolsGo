#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

class Dog():
    def spake(self):
        print("狗在叫")

class Cat():
    def spake(self):
        print("猫在叫")

class Dir():
    def spake(self):
        print("其他在叫")


def mytest(obj):#同一操作
    obj.spake()

d=Dog()
c=Cat()
di=Dir()
mytest(d)
mytest(c)
mytest(di)

#案例:写一个操作(函数),传入三个不同的对象,打印不同的颜色
class A():
    def printColor(self):
        print("我是红色")

class B():
    def printColor(self):
        print("我是黄色")

class C():
    def printColor(self):
        print("我是白色")

def test(obj):
    obj.printColor()


test(A())
test(B())
test(C())



