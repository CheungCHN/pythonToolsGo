#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

seq='-'
str=('a','b','c')
print(seq.join(str))

#案例:用户输入了字符串' 安妮 abc123 女 ',请获取'安妮','abc123','女'
#并最终打印 用户名:安妮-密码:abc123-性别:女
#string=input("请输入一个字符串:")
string='安妮 abc123 女'
print(string)
a='用户名:'+string.split()[0]
print(a)
b='密码:'+string.split()[1]
print(b)
c='性别:'+string.split()[2]
print(c)
dd=(a,b,c)
d='-'
e=d.join(dd)
print(e)