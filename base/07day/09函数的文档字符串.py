#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
def add(a,b):
    '''这个函数有加法功能'''
    return a+b
print(add.__doc__)

help(add)
help(print)
#案例:写一个有文档字符串的函数，该函数有加减乘除的功能，并说明传入参数的方式
def mytest(a,b,str):
    '''该函数拥有加减乘除的功能,第一个和第二个参数传入值,第三个参数传入符号'''
    if str=='+':
        return a+b
    elif str=='-':
        return a - b
    elif str == '*':
        return a * b
    elif str == '/':
        return a / b
    else:
        print("输入的信息错误")
        return

e=mytest(1,2,'+')
print(e)
print(mytest.__doc__)
