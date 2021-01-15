#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
'''
and 与 有假为假
or  或 有真为真
not 非,真变为假,假变为真
'''
'''
a=True
b=False
print(a and b)
print(a or b)
print(not a)
'''
#案例:如a=10,b=20,计算(a>b and b<a) or (not(a>b) and b<10)的结果,要计算过程
a=10
b=20
#假 and 假 -->假
#假 or 真    not(假)-->真
#假 or (真 and 假)
#假 or 假
#假
print((a>b and b<a) or (not(a>b) and b<10))
#案例:有字符串'用户名:Maker,密码:123456',验证用户名第一个字母为大写,密码为纯数字.两个条件
#达到,就打印True,否则打印False
str='用户名:Maker,密码:123456'
s1=str.split(',')[0]
print(s1)
s2=s1.split(':')[1]
print(s2)

x1=str.split(',')[1]
print(x1)
x2=x1.split(':')[1]
print(x2)
print(s2[0].isupper() and x2.isdigit())




