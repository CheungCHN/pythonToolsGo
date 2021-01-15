#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
mylist=[8,7,2,1,9,10]
print(mylist)
mylist.reverse()#倒着输出
print(mylist)

mylist.sort()#升序
print(mylist)
mylist.sort(reverse=True)#降序
print(mylist)
#案例:从终端输入信息,这些信息组成一个列表,然后对列表进行排序
# a=input("请输入信息")
# mylist2=[]
# mylist2.extend(a)
# print(mylist2)
# mylist2.sort()
# print(mylist2)


#案例:将属于list1 = ["a1","a2","a3","a4","a5","a6","a7"]，
# 但不属于list2 = ["a1","a3","a4","a6"]的所有的元素组成一个新的列表list3。
list1=["a1","a2","a3","a4","a5","a6","a7"]
list2=["a1","a3","a4","a6"]
list3=[]
for i in list1:
    if i not in list2:
        list3.append(i)
print(list3)

# for i in list1:
#     for j in list2:
#         if i==j:
#             break
#     else:
#         list3.append(i)
# print(list3)


#案例:创建一个包含字符串和数字的列表，打印出第3到5个元素，倒数第3个元素。
mylist2=['qianfeng',666,'aaa',999,777,888,20.22,'bbb']
print(mylist2[2:5])
print(mylist2[-3])

