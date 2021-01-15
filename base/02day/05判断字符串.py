#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
a='fdaffdfHHHafda23243afa'
print(a.isdigit())#a为纯数字返回True,否则返回False
print(a.isupper())#a为纯大写字母返回True,否则返回False
print(a.islower())#a为纯小写字母返回True,否则返回False
print(a.isspace())#a为纯空格时返回True,否则返回False
print(a.isalpha())#a为纯字母时返回True,否则返回False
print(a.isalnum())#a为字母或数字时返回Ture,否则返回False

#案例:从终端输入一个密码,要求只能是字母或数字,如果符合要求打印True,不符合要求打印False
s=input("请输入密码:")
print(s.isalnum())
#案例:从终端输入电话号码,判断输入是否合法,是打印True,不合法打印False
s2=input("请输入电话号码:")
print(s2.isdigit())

