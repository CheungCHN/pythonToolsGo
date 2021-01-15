#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
a=10
print("a=%d"%a)#要把a变量里的值替代字符串中%d
b=20.22
print("b=%f"%b)
c='我是字符串'
print("c=%s"%c)

print("a=%d,b=%f,c=%s"%(a,b,c))

str='20.2222222'
f=float(str)
print(f)
print("小数点后两位%.2f"%f)

#案例:定义两个变量,一个是整数型,一个是字符串类型,赋值你的年龄和姓名,用占位符打印出来
x=18
y='maker'
print("年龄:%d,姓名:%s"%(x,y))

#案例:已知A网站苹果和橘子两种水果单价(具体如下)，用户根据自己的需求输入斤数， 系统计算总价并打印结果
# 水果单价
#apple_price = 6.6
#orange_price = 5
'''
a_f=float(input("请输入苹果的斤数:"))
j_f=float(input("请输入橘子的斤数:"))
r=a_f*6.6+j_f*5
print("请付:%.2f"%r)


#案例:用户登录系统：用户输入用户名和密码， 并控制台格式化输出用户输入的用户名和密码。
usr_name=input("请输入用户名:")
usr_passwd=input("请输入密码:")
print("用户名:%s,密码:%s"%(usr_name,usr_passwd))
'''

#查看内置函数的使用方法
help(print)
