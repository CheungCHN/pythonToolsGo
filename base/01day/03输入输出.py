#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
'''
1.输出print("str")
	1.print默认输出是换行
	2.如果不要换行,在尾部添加end=""
	3.print("hel\nlo world"),\n也可以换行
	4.()里可以写字符串,变量,表达式
2.输入input()
	1.默认返回的是字符串
	2.会堵塞程序运行
'''
'''
print("我是自动换行的")
print("我不会自动换行",end="")
print("上面的换行了吗?")
print("aaaaa\nbbbbb")
x=input("请输入你的姓名:")
print(x)
y=input("请输入你的年龄:")
print(y)

print(type(y))#查看变量的数据类型
yy=int(y)#数据类型转换
print(type(yy))
'''

#1.从屏幕接收两个整数，并打印其加减的结果
'''
a=input("请输入一个整数:")
b=input("请输入另一个整数:")
d=int(a)+int(b)
print(d)
d1=int(a)-int(b)
print(d1)
'''

'''
2.一个print显示以下内容:
姓名:葫芦娃
年龄:12
性别:男
地址:葫芦山
'''
print("姓名:葫芦娃\n年龄:12\n性别:男\n地址:葫芦山")

#3,使用两个print打印下面一句话
#'我们都是葫芦娃,葫芦娃啊葫芦娃'
print('\'我们都是葫芦娃,',end="")
print('葫芦娃啊葫芦娃\'')

