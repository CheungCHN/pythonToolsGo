#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
#不可变类型,改变形参的内容,实参不受影响
# def test01(a):#a=(1,2,3)
#     print(a)
#     a=10
#     print(a)
#
# a1=100
# test01(a1)
# print(a1)
#
# b1=(1,2,3)
# test01(b1)
#可变型,改变形参的内容,实参也会受到影响
def test02(mylist,mydict):
    mylist[2]=100
    mydict[2]=200

list1=[1,2,3]
dict1={1:10,2:20,3:30}
test02(list1,dict1)
print(list1)
print(dict1)


#案例:定义一个字典,键是1,2,3,4,5,值都是0,通过一个函数改变这个字典,让他的值为10,20,30,40,50
dd={1:0,2:0,3:0,4:0,5:0}

def mytest(dd):
    a=dd.keys()
    for i in a:
        # print(i)
        dd[i]=i*10

mytest(dd)
print(dd)#{1:10,2:20,3:30,4:40,5:50}