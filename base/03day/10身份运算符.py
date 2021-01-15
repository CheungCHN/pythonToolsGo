#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
a=10
b=a
print(id(a))
print(id(b))
b=20
print(id(a))
print(id(b))
print(a is b)
print(a is not b)
#案例:a1=10,b1=2.经过运算,b1+=8,判断a1和b1是否引用自一个对象
a1=10
b1=2
b1+=8
print(id(a1),id(b1))
print(a1 is b1)
#案例:有变量s='abc',s2='123abc',获取s2字符串中的abc赋值给s3变量,然后判断s和s3是否引用自一个对象
s='abc'
s2='123abc'
s3=s2[3:6]
print(id(s),id(s3))
print(s is s3)


