#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
#
# a1=10
#
# for i in range(10):
#     print(i)
#
# a=i+10
# print(a)
#
# while 1:
#     b=20
#     if a>20:
#         break
#     a+=1
#
# print(b)
#
# if 20>10:
#     c=30
# print(c)
#
# def test():
#     d=40
#
# test()
# print(d)

# def test02(aa1,bb2):
#     #print(aa,bb)
#     aa=aa1
#     bb=bb2
#     return aa,bb
#
# a,b=test02(100,200)
# print(a,b)

a=10#全局变量

def test():
    # b=20
    global a#在函数内使用全局变量,要加global
    a=20
test()
print(a)

#案例:定义一个全局变量，一个for里的变量，一个函数内的局部变量
my=10#全局变量

for i in range(10):
    aaa=20

def mytest():
    bb=20
    print(bb)







