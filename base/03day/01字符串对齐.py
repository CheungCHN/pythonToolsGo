#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
str='小明'
print(str.center(50,'*'))
print(str.ljust(50,'?'))
a='*'
print(str.rjust(50,a))
'''
#案例:打印以下图形
    **
**
        **
    **
'''
str1='**'
print(str1.center(10,' '))
print(str1.ljust(10,' '))
print(str1.rjust(10,' '))
print(str1.center(10,' '))
#案例:打印左边50个x,右边50个x,中间是hello
ss='hello'
print(ss.center(105,'x'))


