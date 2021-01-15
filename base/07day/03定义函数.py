#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
#定义函数
def test():
    print("我是函数")#2 6

#调用函数
test()#1 3

def test02():
    test()#5 7

test02()#4 8

# 案例:
# 1.写一个函数add，接受两个整数作为参数，返回这两个整数的和。
def add(a,b):
	c=a+b
	return c

d=add(10,20)
print(d)
# 2.声明一个函数，实现求1+2+3+...+N的和,如:终端输入10,函数返回1-10的和


def mytest():
	n=int(input('请输入一数字:'))
	d=0
	for i in range(n+1):
		d=d+i
	return d

m=mytest()
print(m)
