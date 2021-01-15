#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
class A():
    def printA(self):
        print("---------A----------")

    def printKK(self):
        print("----------A KK----------")


class B():
    def printB(self):
        print("---------B----------")

    def printKK(self):
        print("----------B KK----------")

class C(A,B):#多继承
    def printC(self):
        print("---------C----------")

    def printKK(self):
        print("----------C KK----------")

c=C()
c.printA()
c.printB()
c.printC()

c.printKK()#当父类中有同名方法时,先调用先继承的父类中的方法
print(C.__mro__)


