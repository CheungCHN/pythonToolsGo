#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
#定义一个变量
a=10
print(a)
print(type(a))
a='str'
print(type(a))
#定义多个变量,然后赋相同的值
a1=b1=c1=100
print("a1=%d,b1=%d,c1=%d"%(a1,b1,c1))
#定义多个变量,然后赋不相同的值
name,age,score='小明',18,80.88
print("name=%s,age=%d,score=%f"%(name,age,score))

'''
案例:
	1.给三个变量同时赋值20,并打印出来
	2.把以下数据一次性赋给不同的变量中,并打印
	'公司:华为',8,'地址:深圳
'''
a2=b2=c2=20
print(a2,b2,c2)
s1,s2,s3='\'公司:华为\'',8,'地址:深圳'
print(s1,s2,s3)

c2=a2+b2
