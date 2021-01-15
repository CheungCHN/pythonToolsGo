#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
class Maker():
    #构造函数
    def __init__(self,name,age):
        self.__name=name#定义私有成员
        self.__age=age#定义私有成员
        self.score=90

    def __pri(self):#私有方法
        print("要分数达到95分以上才可以看我名字%s,我的年龄%d"%(self.__name,self.__age))

    def looktest(self,sc):
        if sc>=95:
            self.__pri()

m=Maker('小明',18)
# print(m.__name)#类的外部不能访问私有成员
# print(m.__age)
print(m.score)
# m.__pri()#类外部能访问私有方法
m.looktest(80)

#案例:设计一个类,有私有对象属性name,age,设计类方法,有r权限就可以读取这两个私有属性,
#有w权限就可以修改这两个属性
class Maker2():
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def __pri(self):#打印姓名和年龄的私有方法
        print("姓名:",self.__name,'年龄:',self.__age)

    def __SetN_A(self,name,age):#修改姓名和年龄的私有方法
        self.__name=name
        self.__age=age

    def test(self,str,name='',age=0):
        if str=='r':
            self.__pri()#如果是r权限,那么就调用打印姓名和年龄的私有方法
        elif str=='w':
            self.__SetN_A(name,age)
        else:
            print("请输入正确的权限")


n=Maker2('小明',18)
n.test('r')
n.test('w','小花',20)
n.test('r')