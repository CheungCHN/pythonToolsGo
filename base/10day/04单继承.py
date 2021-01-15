#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
#父类(基类)
class Father():
    a=10
    b=20

#子类(派生类)
class Son(Father):
    c=30

s=Son()#定义子类对象
print(s.a,s.b,s.c)

class Father2():
    house='150平'
    car='BMW'
    money='2个小目标'
    __coff='10个小目标'
    def fun(self):
        print("会吟诗")

    def fun2(self):
        print('会赚钱')

    def fun3(self):
        print("会抽华子")

    def __fun4(self):
        print("会约人")

class Son2(Father2):
    pass

s2=Son2()
print("我是富二代,我有:",s2.house,s2.car,s2.money)
# print(s2.__coff)#不能继承父类的私有属性
s2.fun()
s2.fun2()
s2.fun3()
# s2.__fun4()#不能继承父类的私有方法

#案例:定义一个动物类,属性有name,age.方法有会走move,会叫spake.定义一个猫和狗类,继承动物类
#通过猫对象调用move和spake方法,分别是age岁的name猫在走,age岁的name猫在叫,狗也一样
class Animal():
    name=''
    age=0
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def move(self,mystr):
        print(self.age,'岁的',self.name,mystr,'在走')

    def spake(self,mystr):
        print(self.age,'岁的',self.name,mystr,'在叫')

class Cat(Animal):
    pass

class Dog(Animal):
    pass

c=Cat('波斯',2)
d=Dog('柯基',3)

c.move('猫')
c.spake('猫')
d.move('狗')
d.spake('狗')