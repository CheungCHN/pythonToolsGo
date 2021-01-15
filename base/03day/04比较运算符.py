#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
a=10
b=20
print(a>b)
x='edla'
y='db'
print(x>y)#False
#案例:从终端输入2个数字,比较大小
'''
a1=int(input("请输入一个数字:"))
b1=int(input("请输入另一个数字:"))
print(a1>b1)
'''
#案例:从终端输入一个3位数的数字,获取最大的数字和最小的数字的和.用到if语句
#如:123 ,,,1+3=4
m=input("请输入一个三位的数字:")
m1,m2,m3=int(m[0]),int(m[1]),int(m[2])
d=0
if m1>m2:
    d=m1
else:
    d=m2
#到这d是m1和m2之间更大的数
if d>m3:
    pass
else:
    d=m3

print("最大数:",d)
q=0
if m1<m2:
    q=m1
else:
    q=m2

if q<m3:
    pass
else:
    q=m3

print("最小的数:",q)
print(d+q)

