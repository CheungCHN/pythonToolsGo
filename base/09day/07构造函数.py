#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
#定义对象时,通过类名(实参)->__init__(形参)
class Maker():
	def __init__(self,name):
		print(name)

m=Maker('小明')

#构造函数给对象属性赋初始值
class Maker2():
	def __init__(self,name):
		self.name=name

m2=Maker2('小明')
print(m2.name)

# 案例:
# 声明一个Dog类，
# 1)拥有属性：名字、年龄、性别和品种；
#
# 要求创建对象的时候名字、品种必须赋值，
#
# 年龄和性别可以赋值也可以不赋值
#
# 2)拥有两个对象方法，一个用来打印狗的信息(显示信息的方法)
#
# 一个叫唤的方法:以'XXX:汪汪汪汪'的格式打印叫唤信息
class Dog():
    def __init__(self):
        self.name='旺财'
        self.breed='拉布拉多'
        self.age=18
        self.sex='女'

    def printDog(self):
        print('名字:%s'%self.name,'品种:%s'%self.breed,'年龄:%d'%self.age,'性别:%s'%self.sex)

    def spake(self):
        print(self.name+':汪汪汪汪')
d=Dog()
d.printDog()
d.spake()