#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
mylist=[[1,2,3],[4,5,6],[7,8,9]]
print(mylist)
for i in mylist:
   for j in i:
       print(j,end="")
   print()

'''
案例：按照下方二维表创建二维列表，并用for循环输出
人名    年龄    年代    
西施    16    春秋战国    
貂蝉    18    三国    
王昭君    20    汉    
杨玉环    19    唐  
'''
list=[['人名','年龄','年代'],['西施',16,'春秋战国'],['貂蝉',18,'三国'],['王昭君',20,'汉'],['杨玉环',19,'唐']]
for i in list:
    for j in i:
        print(j," ",end="")
    print()

