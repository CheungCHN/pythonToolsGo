#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
class Maker():
    def __init__(self,v):
        self.v=v

    #直接打印对象,那么这个函数的返回值会被打印
    def __str__(self):
        msg="我是魔法方法的返回值"
        return msg

    def __add__(self,ot):
        print("两个对象相加")
        return f'{self.v}{ot.v}'

    def __lt__(self,ot):
        print('小于')
        if self.v<ot.v:
            print('前面的更小')
        else:
            print("前面的更大")
        return self.v<ot.v


m=Maker('aaa')
print(m)
m1=Maker('bbb')
print(m1)
print(m+m1)

#lt  小于(两个对象比较时调用)
#案例:定义一个魔法方法,比较两个对象的大小
n=Maker(10)
n2=Maker(20)
if n<n2:
    print("n<n2")