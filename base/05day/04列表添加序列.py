#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
# a=[3,4,5]
# mylist=[1,2]
# mylist.extend(a)
# print(mylist)
# mylist.extend([8,9])
# print(mylist)
#
# str='hello'
# str2='world'
# b=[1,2,3]
# b.append(str)
# print(b)
# b.extend(str2)
# print(b)

#mylist.extend(10,11) 报错,不能这样添加

#案例:从终端中输入5个数字,以空格分开,然后把这些数字组成一个列表,然后加入到mylist2=[1,2,3,4,5]列表中
#注意,要把列表中字符数字变为数字
# mylist2=[1,2,3,4,5]
# s=input("请输入一个5位数字,以空格分开:")
# mylist3=s.split()
# print(mylist3)
# mylist4=[]
# for i in mylist3:
#     mylist4.append(int(i))
# print(mylist4)
# print(mylist2+mylist4)

#空列表可以通过添加序列的方式加入数据吗?可以
mylist5=[]
mylist5.extend([1,2,3])
print(mylist5)

#8.列表中添加序列是否能在()里直接写字符串?
mylist5.extend(['hello'])
print(mylist5)

