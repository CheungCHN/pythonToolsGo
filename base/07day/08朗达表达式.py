#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
a=lambda x:x*2
print(a(3))

#lambda表示做为另一个函数的实参使用
def test(a,b,opt):#a=1,b=2,opt=lambda x,y:x+y
    print("a=",a)
    print("b=",b)
    print("结果:",opt(a,b))

test(1,2,lambda x,y:x+y)

#案例:定义一个加法的lambda函数,然后调用使用
add=lambda x,y:x+y
print(add(2,3))
#案例:编写一个lambda函数，对x和y进行幂运算，并调用此函数
kk=lambda x,y:x**y
print(kk(2,2))