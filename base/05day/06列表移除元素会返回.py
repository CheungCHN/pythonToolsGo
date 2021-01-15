#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

mylist=[1,2,3,4,5,6]
m=mylist.pop()
print(mylist)
print(m)

n=mylist.pop(3)
print(mylist)
print(n)
#案例:有列表['1','2','3','Maker','4','5','ceshi'],有7个元素
#把列表中的非数字字符串移除,并打印移除的字符串,然后计算列表的数字之和
mylist2=['1','2','3','Maker','4','5','ceshi']
# for i in range(6):#i==3
#     if mylist2[i].isalpha():
#         str=mylist2.pop(i)
#         print(str)
#
# print(mylist2)
# s=0
# for i in mylist2:
#     s+=int(i)
#
# print(s)
print("------")
list = ['1','2','3','Maker','4','5','ceshi']
d = 0
for i in list:
    if i.isalpha():
        list.pop(d)
        print(list)
    d=d+1
print(d)