#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
'''
a=10
b=20
print("a的地址:",id(a))#查看变量a的内存地址
print("b的地址:",id(b))
a=b#内部来说,是把b的地址赋值给a
print("a的地址:",id(a))
print("b的地址:",id(b))
'''
#案例:定义两个变量a和c,分别赋值10,20,然后打印它们的地址,之后把a赋值给c,然后打印a的地址
a=10
c=20
print("a的地址:",id(a))
print("c的地址:",id(c))
c=a
print("a的地址:",id(a))
print("c的地址:",id(c))