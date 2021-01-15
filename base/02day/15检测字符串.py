#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
str1="Hello world"
# 检查字符串是否以指定的字符串开头
print(str1.startswith('He'))  # True
# 检查字符串是否以指定的字符串结尾
print(str1.endswith('lo'))  # True
# 获得字符串首字母大写
print(str1.capitalize())  # Hello, world!
# 获得字符串变大写
print(str1.upper())  # HELLO, WORLD!
#str中所有大写转小写
print(str1.lower())
#把字符串的每个单词首字母大写
print(str1.title()) #Hello,World
s=str1.upper()
print(s)

#案例:把字符串'HELLO,WORLD!'变为小写,然后把单词的首字母变为大写
str2='HELLO,WORLD!'
s2=str2.lower()
s3=s2.title()
print(s3)
#案例:有字符串'192.168.18.22:8080',检测该字符串是否以192.开头,80结尾
str3='192.168.18.22:8080'
print(str3.startswith('192.'))
print(str3.endswith('80'))


