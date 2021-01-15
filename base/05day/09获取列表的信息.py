#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
mylist=[1,2,3,4,5,6]
print("len:",len(mylist))
print(max(mylist))
print(min(mylist))
mylist2=['a','b','c','a']
print(max(mylist2))
print(min(mylist2))
print(mylist.index(3))
print(mylist2.count('a'))
#案例:从终端上输入N位数,组成列表,获取列表长度,最大,最小值,最大值在对应的索引,最小值出现的次数
str=input("请输入数据:")
list=[]
#list.extend(str)
for i in str:
    list.append(i)
print(list)
print(max(list))
print(min(list))
print(list.index(max(list)))
print(list.count(min(list)))