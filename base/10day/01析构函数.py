#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
# class Animal():
#     def __init__(self,name):
#         print("构造函数被调用")
#         self.name=name
#
#     def __del__(self):#析构函数
#         print("析构函数")
#         print("%s对象马上被干掉了"%self.name)
#
# dog=Animal('旺财')
# print(dog.name)
#
# #删除对象
# del dog
#
# a=input("aaaa:")

# 5.当1个变量保存了对象的引用,此时对象引用计数器就加1,
# 当使用del删除变量指向的对象时,引用计数器就减1,当减到0时,就调用析构函数


class Dog():

    def __init__(self,name):
        print("构造函数被调用")
        self.name=name

    def __del__(self):#析构函数
        print("析构函数")
        print("%s对象马上被干掉了"%self.name)




d1=Dog('小黄')#计数器1
# d2=d1#计数器2
# d3=d1#计数器3
# print('d1=',d1)
# print('d2=',d2)
# print('d3=',d3)


del d1#计数器2

# del d2#计数器1
# del d3#计数器0
# a=10
# del a
# print(a)

#休眠代码运行
import time

# print("我是打印的第一句话")
# time.sleep(2)
# print("我是第二句话")
# time.sleep(3)
# print("我是第三句话")
# time.sleep(1)
# print("我是第四句话")

#案例:写一个运行后10秒结束的程序,程序中定义5个变量,一个对象,当对象删除时,这5个变量也要被一起删除
a1=10
class Maker():
    def __del__(self):
        print("maker析构函数")
        del self.name
        del self.a


m=Maker()
m.name='aaaa'
m.a=a1
print(id(a1))
print(id(m.a))
del m
print(a1)

time.sleep(2)




