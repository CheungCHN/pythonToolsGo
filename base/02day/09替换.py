#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
name='hello world python haha hello'
print(name.replace('hello','HELLO'))
print(name.replace('hello','HELLO',1))

#案例:获取字符串str="曾今有一段真诚的爱情摆在我面前,我没有珍惜,我很后悔,如果上天再给我一次机会",
#替换字符串中所有的'我'为'俺',但保留最后一个'我'
str='曾今有一段真诚的爱情摆在我面前,我没有珍惜,我很后悔,如果上天再给我一次机会'
w='我'
n=str.count(w,0,len(str))
print(str.replace('我','俺',n-1))