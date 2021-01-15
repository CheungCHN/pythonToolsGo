#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
#定义元组
tup1=('maker','qianfeng',18,1999)
print(tup1)
tup2=(1,2,3,4)
tup3='a','b','c'
tup4=1,2,3,4
print(tup4)
#只有0个或1个元素时
tup5=()
tup6=(88,)
tup7=(66)
print(type(tup6))#元组
print(type(tup7))#int

print(tup1[0])
print(tup1[2:4])

t1=(1,2,3,4)
#t1[0]=88 不能修改
print(t1)
t2=(1,2,[3,4,5],6)
print(t2)
t2[2][1]=88
print(t2)

# 案例: 创建一个元组A, 里面的元素是整数, 创建一个只有一个元素的元组B,
# 创建一个元组C, 里面的元素有其中一个是列表
A=(1,2,3,4,5)
B=(66,)
C=('a','b',[1,2,3,4])

# 案例: 在上个案例的基础上, 打印三个元组.然后修改C元组中的列表中的值,在打印
print(A)
print(B)
print(C)
C[2][2]=88
print(C)
# 案例:现有列表：(tuple)
# name_list =["tom","kaisa","alisi",["xiaoming","songshu"]]
# 现在有个要求，将最外层的列表转换成元组存储，里面的小列表不变；
# 并且向小列表中添加一个元素“python”
name_list =["tom","kaisa","alisi",["xiaoming","songshu"]]
name_tuple=tuple(name_list)
print(name_tuple)
name_tuple[3].append('python')
print(name_tuple)