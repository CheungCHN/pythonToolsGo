#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
str1="hellofaffasdfworlddasf"
print(str1.find('world',0,len(str1)))#从0开始计算 13
print(str1.find('maker'))

#案例:有字符串'192.168.88.66:8808?id=01&user=maker&passwd=123abc&ipthon=13866888666&
#email=7634773@qq.com&qq=7634773&wx=weixi\\n123abc',获取ipthon的值
str='192.168.88.66:8808?id=01&user=maker&passwd=123abc&ipthon=13866888666&\
email=7634773@qq.com&qq=7634773&wx=weixi\\n123abc'
pos=str.find('ipthon')
print(pos)
v=len('ipthon=')
print(v)
n=pos+v
print(str[n:n+11])

ss=str.split('=')[4]
print(ss.split('&')[0])