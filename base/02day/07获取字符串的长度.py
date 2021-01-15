#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
str="hello world"
a=len(str)
print(a)
print(len(str))

#案例:获取字符串'软件测试,自动化测试'的长度,结合切片把自动化测试截取出来赋值给一个变量,然后打印
mystr='软件测试,自动化测试'
print(len(mystr))
b=mystr[5:len(mystr)]
print(b)
#案例:从终端输入一字符串,截取后5个字符组成另一个字符串
mystr2=input("请输入一个字符串:")
print(len(mystr2))
c=mystr2[len(mystr2)-5:len(mystr2)]
print(c)