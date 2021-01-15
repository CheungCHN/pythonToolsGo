#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
a=10
b=21
print("a*b=",a*b)#210
print('a'*3)#aaa
a1=10
b1=2
print(a1**b1)#100
a2=10
b2=3
print(a2//b2)#3
#案例:有变量a=30,b=4,获取它们的乘积和除后的整数之和,打印3遍
a3=30
b3=4
c3=a3*b3
d3=a3//b3
e=c3+d3
e2=str(e)
print(e2*3)

#案例:从终端输入两个数,一个数的基数,另一个数的幂数,打印结果
#如输入3和2,打印9  3^2=9
a4=int(input("请输入一个数字:"))
b4=int(input("请输入另一个数字:"))
print(a4**b4)

#案例:从终端输入5位数字,计算他们的和.如:12345 他们的和是15
mystr=input("请输入一个5位的数字:")
x1=int(mystr[0])
x2=int(mystr[1])
x3=int(mystr[2])
x4=int(mystr[3])
x5=int(mystr[4])
print(x1+x2+x3+x4+x5)


