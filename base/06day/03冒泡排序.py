#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import random
mylist=[]
for i in range(10):
    mylist.append(random.randint(0,20))
print(mylist)

for i in range(len(mylist)-1):
    for j in range(len(mylist)-1-i):
        if mylist[j]<mylist[j+1]:
            mylist[j],mylist[j+1]=mylist[j+1],mylist[j]

print(mylist)

arr=[3,2,8,1]
print(len(arr))
for i in range(len(arr)-1):#2  range(3)
    for j in range(len(arr)-1-i):#j==0 range(1)
        if arr[j]<arr[j+1]:#8<3
            arr[j],arr[j+1]=arr[j+1],arr[j]
'''
i==0
j==0
j==1
[3,8,2,1]
[8,3,2,1]
'''

'''
1.外循环是长度-1
2.内循环是长度-1-i
3.是arr[j]和arr[j+1]进行比较
4.交换是arr[j]->arr[j+1]及arr[j+1]->arr[j]
'''
#案例:从终端输入产生随机数的个数,使用随机数给一个列表赋值,然后对列表进行冒泡排序
a=int(input("请输入一个数字:"))
mylist2=[]
for i in range(a):
    mylist2.append(random.randint(0,9))
print(mylist2)

for i in range(len(mylist2)-1):
    for j in range(len(mylist2)-1-i):
        if mylist2[j]<mylist2[j+1]:
            mylist2[j],mylist2[j+1]=mylist2[j+1],mylist2[j]

print(mylist2)