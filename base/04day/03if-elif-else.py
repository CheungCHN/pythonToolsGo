#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

a=10
b=20

if a>b:
    print('a>b')
elif a<b:
    print('a<b')
else:
    print('a=b')
# 案例:根据控制台输入的成绩，输出对应的等级
# 	90以上：优秀
# 	80~90：良好(包含80)
# 	60~80：还行(包含60)
# 	60以下：加油吧，少年
#
m=int(input("请输入一个分数:"))
if m>90:
    print("优秀")
elif 90>m>=80:
    print("良好")
elif 80>m>=60:
    print("还行")
elif m<60:
    print("加油吧，少年")
else:
    print("输入错误")
# #案例:从终端输入一个字符串,判断是否为纯数字,是否为纯大写字母,是否为纯小写字母,然后打印对应的字符串
#str = input("请输入一个字符串:")
str=input("请输入一个字符串:")
if str.isdigit():
    print("数字")
elif str.isupper()and str.isalpha():
    print("大写")
elif str.islower() and str.isalpha():
    print("小写")
else:
    print("输入不合法")

