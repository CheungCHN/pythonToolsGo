#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
#在本文件定义类,也在本文件定义对象
class Maker():
    name='aa'

    def test(self):
        print('maker')

    def __init__(self):
        print("你终于有了对象")

m=Maker()#m是变量也是对象
print(m)
m1=Maker()
print(m1)

#在别的文件定义类,在本文件定义对象
from Car import MyCar
a=MyCar()

# 案例:自己写个类,在本文件中创建对象
class Maker2():
    age=18#变量,成员变量,属性,类属性

    def test(self):#函数,成员函数,成员方法
        print("maker2")

mm=Maker2()#对象

# 案例:把前面写的电脑类添加上__init__函数,通过导入模块的方式导入到本文件来创建对象
from 类的定义 import Pc
pm=Pc()



