#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
#定义一个类,在内存中要花空间吗?
class Maker():
    name='小明'

#定义对象
m=Maker()#m就是对象
#调用类的属性,调用类的类属性
print(m.name)

#给类的属性赋值
m.name='小花'
print(m.name)

m2=Maker()
print(m2.name)

#创建对象属性
m3=Maker()
m3.age=20#age就是对象属性,只有m3可以用
print(m3.age)

m4=Maker()
#print(m4.age)报错,不能使用m3的对象属性

#案例:定义一个学生类,类属性有name,age,然后通过对象修改类属性的值,然后给对象添加属性score,并打印
class Student():
    name='maker'
    age=18

st=Student()
print(st.age)
st.age=20
print(st.age)
st.score=99
print(st.score)
