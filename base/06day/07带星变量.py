#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
a,*b,c,d=(1,2,3,4,5,6,7,8,9)
print(a)
print(c)
print(d)
print(b)
# 案例:
# 1.创建两个元组，进行连接操作。
tup1=(1,2,3,4)
tup2=('a','b','c')
tup3=tup1+tup2
print(tup3)
#
# 2.创建一个列表和元组，将其连接后打印出来(用到元组转换列表),其中列表用变量代码*方式获取
tup4=('a','b','c')
a1,*b1,c1=(1,2,3,4,5)
print(b1)
tup5=tuple(b1)+tup4
print(tup5)