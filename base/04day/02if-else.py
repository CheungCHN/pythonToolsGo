#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
if True:
    print("我是满足条件的")
else:
    print("我是不满足条件的")

a=10
b=20

if a>b:
    print('a>b')
else:
    print('a<=b')

#0000 0000
#
if a>>5 & b:
    print("我是满足条件的")
else:
    print("我是不满足条件的")

print("sss")

mystr='hello'
s='he'
if s in mystr:
    print("我是满足条件的")
else:
    print("我是不满足条件的")

#案例:从控制台输入一个数，判断这个数是否是偶数
m=int(input("请输入一个数字:"))
if m%2:
    print("输入的不是偶数")
else:
    print("输入的是偶数")

#案例:从终端输入用户和密码,如果都正确,打印欢迎登入,如果有一个不正确就打印用户名或密码不正确
#用户名在str1='makermaker2maker3maker4',密码在str2='0001000200030004'
user=input("请输入用户名:")
ps=input("请输入密码:")
str1='makermaker2maker3maker4'
str2="0001000200030004"
if user in str1 and ps in str2:
    print("欢迎登入")
else:
    print("用户名或密码不正确")
