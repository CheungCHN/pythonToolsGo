#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
tup=(1,2,3,4)
del tup
#print(tup)

tup2=(1,2,3,4)
print(len(tup2))
print(max(tup2))
print(min(tup2))
print("--------------")
#案例:求元组(1,2,8,9,22,0,3)的长度,最大值,最小值,然后把元组转换为列表,打印出来,最后删除元组
tup3=(1,2,8,9,22,0,3)
print(len(tup3))
print(max(tup3))
print(min(tup3))
list2=list(tup3)
print(list2)
del tup3

