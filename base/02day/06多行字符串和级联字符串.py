#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

str='''
hello
world
'''
print(str)

str2="""
aaaa
bbbb
"""
print(str2)

print("this"" is"" string")

'''
#字符串综合案例:有字符串'192.168.88.66:8808?id=01&user=maker&passwd=123abc&ipthon=1386688666&
email=7634773@qq.com&qq=7634773&wx=weixi\\n123abc'
1.请用多行字符串方式定义变量
2.请获取ip地址和端口号,并验证是否为纯数字,然后拼接起来,用冒号分开ip和端口号,,并打印出来
3.获取wx的值,并打印
4.获取user和passwd的值,并拼接好打印出来
5.获取电话号码,并判断是否为纯数字,并打印
'''
mystr='''
192.168.88.66:8808?id=01&user=maker&passwd=123abc&ipthon=1386688666&
email=7634773@qq.com&qq=7634773&wx=weixi\\n123abc
'''
print(mystr)
ip=mystr[0:14]
print(ip)
port=mystr[15:19]
print(port)
print(ip.isdigit())
print(port.isdigit())
print(ip+":"+port)
wx=mystr[-14:-1]
print(wx)
u=mystr[31:36]
print(u)
p=mystr[44:50]
print(p)
print(u+p)
i=mystr[58:68]
print(i)
print(i.isdigit())

#1.切片中str[2:4:2]表示什么意思?从第三个字符开始每次跳一个字符截取
str88='abcdefgh'
print(str88[2:4:2])