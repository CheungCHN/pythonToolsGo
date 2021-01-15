#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
#定义类,也是定义数据类型
class Fs():
    #定义属性
    fl=2
    name='钻石'

    #定义方法
    def myFS(self):#参数中有self,那么表明这个函数是成员函数
        print("降温")

#案例:抽象一个汽车,写成类
class Car():
    name='BMW'

    def mytest(self):
        print("代步")



#案例:把电脑抽象出来,写成一个类
class Pc():
    name="苹果"
    cpu='i7'
    ram='16g'
    disc='500g'
    def __init__(self):
        print("我是pc里的函数")

    def test01(self):
        print("看小电影")

    def test02(self):
        print("编程")

    def test03(self):
        print("学习")




