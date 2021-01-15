#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
#必需参数
def show(str,num):
    print(str)
    print(num)
show('maker',18)
#案例:定义一个函数，有三个参数，从终端输入3个数，传入到这个函数，并调用这个函数，打印出参数的内容
# a = input("请输入第一个数据:")
# b = input("请输入第二个数据:")
# c = input("请输入第三个数据:")
#
# def myprint(a,b,c):
#     print(a,b,c)
#
# myprint(a,b,c)
print("-----------")
#关键字参数
def test(name,age):
    print(name)
    print(age+10)

#在调用函数时,传入参数的时候注明数据要给哪个形参
test(age=18,name='maker')
#案例:定一个函数，参数有id,name,age,ipthon,有一个字典
#{'id':1,'name':'maker','age':18,'ipthon':'123234324423'},获取对应的值，传入函数中
dit={'id':1,'name':'maker','age':18,'ipthon':'123234324423'}

def test02(id,name,age,ipthon):
    print(id,name,age,ipthon)

test02(id=dit['id'],name=dit['name'],age=dit['age'],ipthon=dit['ipthon'])

print("============")
#默认参数
def fun(name,age=18):
    print(name,age)

fun('maker')#因为形参age有默认值,那么实参可传可不传
fun('maker',20)#如果传了实参,那么结果以实参为准

def fun2(name,age=18,ipthon='111111'):#因为age有默认值,那么从这个age后面的形参都要有默认值
    print(name,age,ipthon)

fun2('maker')

#案例:定一个函数,打印用户的信息，用户的信息有姓名，性别，年龄，电话，其中性别默认为'男'
def fun3(name,sex='男',age=0,ipthon='0'):
    print(name,sex,age,ipthon)

fun3('maker',age=18,ipthon='13833333333')

#不定长参数
def fun4(name,*arr,age):
    print(name)
    print(arr)
    for i in arr:
        print(i)
    print(age)
fun4('maker',2,3,'ccc','ddd',age=18)
#案例:实现一个函数，支持传入任意多个整数进行加法运算，并返回结果
def adds(*arr):#arr=(1,2,3,4)
    s=0
    for i in arr:
        s=s+i
    # print(s)
    return s

aa=adds(1,2,3)
bb=aa+10
print(bb)

