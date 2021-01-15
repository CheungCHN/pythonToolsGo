#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

d={1:'a',2:'c'}
# 字典的添加修改删除
# 1.添加:d[3]='c'#如果没有键位3的,那么就添加了一对键值对,如果有就是修改值
# 2.修改:
# 3.删除:
# d[1]='c'
# print(d)
d2={1:'a',2:'b',3:'c',4:'d'}
print(d2.pop(4))#d,返回被删除的value值,这里移除键值为4的元素
print(d2)
d2.popitem()#随机删除,一般删除末尾
print(d2)
del d2[1]#删除元素
print(d2)
d2.clear()#清空字典
print(d2)
del d2#删除字典
#print(d2)

#案例:把1-100的单数当成字典的键,偶数当成字典的值,创建一个字典,然后增加{'name':'maker'},
#{1:'one'}数据


#定义一个字典
myd={}
for i in range(1,101):
    if i%2:
        myd[i]=0
    if i%2==0:
        myd[i-1]=i
# print(myd)
myd['name']='maker'
vv={1:'one'}
myd.update(vv)
print(myd)


#案例:上一题的基础上,删除11键元素,返回他的值,然后打印.随机删除上一题的一对键值对,并打印
#然后清空并删除字典

print(myd.pop(11))
print(myd.popitem())
print(myd)
myd.clear()
del myd
