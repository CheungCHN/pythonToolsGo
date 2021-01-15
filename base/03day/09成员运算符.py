#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
'''
成员运算符
in 如果在指定的序列中找到值返回True,否则返回False
not in 如果在指定的序列中没有找到值返回True,否则返回False

#案例:判断'dfsafaqianfengdfasfafd,该字符串中有没有qianfeng
#案例:判断字符串是否为html代码,只需要判断字符串中是否有<html>,<head>,<body>
#如字符串:'<html><head></head><body>fdasfafyfasdfoafasdf</body></html>'
'''
str='abcdef'
x='c'
print(x in str)
print(x not in str)

#案例:判断'dfsafaqianfengdfasfafd,该字符串中有没有qianfeng
str2='dfsafaqianfengdfasfafd'
s='qianfeng'
print(s in str2)
#案例:判断字符串是否为html代码,只需要判断字符串中是否有<html>,<head>,<body>
#如字符串:'<html><head></head><body>fdasfafyfasdfoafasdf</body></html>'
str3='<html><head></head><body>fdasfafyfasdfoafasdf</body></html>'
s1='<html>'
s2='<head>'
s3='<body>'
print(s1 in str3 and s2 in str3 and s3 in str3)
