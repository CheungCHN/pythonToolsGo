#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
#1.创建集合
s=set()#创建空集合
s1={1,2,3,'a','b'}
s2=set([1,2,3])
#s3=set(1,2,3)
s3=set("hello")
print(s2)
print(s3)
print(type(s3))
#2.删除重复
s4={1,1,2,3,1,4,5,4}
print(s4)
#3.成员关系测试
str={"hello","world","qianfeng","maker"}
print(str)
if 'hello' in str:
    print('hello 在str中')
else:
    print('hello 不在str中')

# 案例:从终端输入5位数,以空格隔开,把这5位数存入列表中,剔除重复的数据,打印出来
# #提示,列表转集合,集合转列表
mystr=input("请输入5位数,以空格隔开:")
mylist=mystr.split()
ss=set(mylist)
print(ss)
mylist2=list(ss)
print(mylist2)
