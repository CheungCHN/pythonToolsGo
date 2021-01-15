#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
a=10
b=20
c=(a if(a>b) else b)
print(c)

#案例:输入三个数，输出其最大者。
x=int(input("请输入第一个数:"))
y=int(input("请输入第二个数:"))
z=int(input("请输入第三个数:"))

x1=(x if(x>y) else y)
y1=(x1 if(x1>z) else z)
print(y1)

