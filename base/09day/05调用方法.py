#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
class Maker():

    def test01(self):
        print("我是Maker")

    def test02(self,name):
        print("我是%s"%name)

    def test03(self,name,age):
        print("我是%s"%name+'我%d'%age)

#定义一个对象
m=Maker()
m.test01()
m.test02('葫芦娃')
m.test03('小林',13)

#通过调用方法来修改成员属性
class Maker1():
    name='aa'
    age=18

    def test(self,Name,Age):
        self.name=Name
        self.age=Age

mm=Maker1()
mm.test('小悟空',12)
print(mm.name)
print(mm.age)

mm2=Maker1()
print(mm2.name)
print(mm2.age)



class Maker3():
    a=18

    def test(self):
        return self.a

mmm=Maker3()
print(mmm.test())

'''
案例:定义一个学生类。有下面的
属性：
1 姓名
2 年龄
3 成绩（语文，数学，英语)[每课成绩的类型为整数]
类方法：
1 获取学生的姓名：get_name() 返回类型:str
2 获取学生的年龄：get_age() 返回类型:int
3 返回3门科目中最高分数的课程。get_course()
4 返回该学生的平均成绩get_avg()
'''
class Student():
    #定义属性
    name='小花'
    age=18
    y=90
    s=100
    e=88
    #定义方法:
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_course(self):
        return max(self.y,self.s,self.e)

    def get_avg(self):
        a=(self.y+self.s+self.e)/3
        return a

ss=Student()
print("-------------")
print(ss.get_name())
print(ss.get_age())
print(ss.get_course())
print(ss.get_avg())