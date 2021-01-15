#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
class Maker():
    age=18
    a=18
    def test(self):
        print("test")
        self.age=20

    #定义类方法
    @classmethod
    def mytest(cls):
        cls.a=88
        print("我是类方法")

# m=Maker()
# m.test()
# Maker().test()
# Maker().mytest()
# Maker.mytest()#调用类方法
# # Maker.test()报错
#
# print(m.age)
# m.test()
# print(m.age)
# m1=Maker()
# print(m1.age)
print("----------")
m2=Maker()
print(m2.a)
Maker.mytest()
print(m2.a)

m3=Maker()
print(m3.a)


