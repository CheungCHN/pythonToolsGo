#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
a=10
b='10'
c=20.52
sa=str(a)
print(type(sa))
sb=int(b)
print(type(sb))
sc=int(c)
print(sc)
print(type(sc))

#type和isinstance的区别
class A:#类,类也是数据类型
    pass

class B(A):#类
    pass

print(isinstance(B(),A))
print(type(B())==A)

#案例:输入一个半径，计算出圆的周长和面积,结果只保留整数部分
'''
n=int(input("请输入一个半径:"))
z=2*n*3.14
print("周长是:",int(z))
s=n*n*3.14
print("面积是:",int(s))
'''
#案例:输入两个数字a，b，计算a与b之和与a与b之差的乘积
'''
a1=int(input("请输入一个数字:"))
b1=int(input("请输入另一个数字:"))
print((a1+b1)*(a1-b1))
'''
#案例:有字符串'abcd4234732helloworld',截取字符串中的数字前2位和后两位,然后相加,打印得出的结果
str='abcd4234732helloworld'
my1=int(str[4:6])
my2=int(str[9:11])
print(my1+my2)