#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
str="hello"
str2="world"
print(str+str2)
print((str+str2)*2)

str3='hello'
#str3[0]='m'
print(str3)
str3='world'
print(str3)
#案例:定义一个变量,变量的值是'你好,约吗?',再定义一个变量,变量的值是'叔叔,我们不约',然后把这两个变量的值连接起来打印出来,然后使用*打印三次
str4='你好,约吗?'
str5='叔叔,我们不约'
print((str4+str5)*3)
#案例:从终端输入用户名的值，密码的值,把这两个信息储存到2个变量，然后整合成
#'用户名:葫芦娃&密码:xiaohudie',打印出来
'''
str6=input("请输入用户名:")
str7=input("请输入密码:")
str8='用户名:'+str6+'&密码:'+str7
print(str8)
'''
#案例:从终端输入2次123,一个是整型，一个是字符串，分别乘以3,分别打印结果
str9=int(input("请输入数字:"))
str10=input("请再次输入数字:")
print(str9*3)
print(str10*3)


#案例:定义一个变量,变量的值为你的名字,然后尝试修改你的姓,看看有什么反应
s='刘maker'
#s[0]='黄'
print(s)