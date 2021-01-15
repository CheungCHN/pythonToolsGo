#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
str1='你好啊!学习累吗? 加油!高薪就在前面,冲鸭!xxx'
str='!'
mystr=str1.split(str)
print(mystr)
print(mystr[0])
print(str1.split(str)[1])
print(str1.split())
#案例:有字符串'192.168.1.22:8808?id=88&user=maker&passwd=123456'
#获取id,user,passwd的值,并拼接打印
s1='192.168.1.22:8808?id=88&user=maker&passwd=123456'
d1=s1.split('=',1)[1]
print(d1)
d2=d1.split('&',1)[0]#88
print(d2)
d3=d1.split('&',2)[1]
print(d3)
d4=d3.split('=')[1]#maker
print(d4)
d5=d1.split('=')[2]#123456
print(d5)
print(d2+d4+d5)

