#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import random
a=random.randint(0,9)#包头包尾
print(a)

mylist=[]
for i in range(10):
    b=random.randint(0,9)
    mylist.append(b)

print(mylist)

mystr=[1,2,3,4]
mystr[0],mystr[1]=mystr[2],mystr[3]
print(mystr)



