#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

mylist=[1,2,3,4]
mylist.insert(7,88)#超过下标数,就插入到末尾,如果添的是负数从右往左数,数据是往右推
print(mylist)
#案例:有列表list=[1,2,4,7,10,18],从终端输入一个数字,插入到指定位置
#如,你输入的是8,那么插入list列表后[1,2,4,7,8,10,18]
list=[1,2,4,7,10,18]
a=int(input("请输入一个数字:"))#3
d=0
for i in list:#2
    if i>a:
        break

    d+=1
list.insert(d,a)
print(list)