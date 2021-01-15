#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
mylist=[1,2,3,4]
mylist.clear()
print(mylist)
#案例:从终端输入一个5位数的数字,存储到列表中,如果不是数字,提示重新输入,只到输入正确为止
#输入正确提示输入正确并打印列表
# 如:123a4,重新输入,如果有一个没输入正确,就重新输入
#
# 如:123a4,那么就存储1234
while True:
    a = input("请输入一个5位数字:")
    mylist2 = []
    b=0#记录有多少个数字存储到列表
    for i in a:
    #判断是否是数字,如果是数字就存储到列表中
        if i.isdigit():
            #存储到列表中
            mylist2.append(int(i))
            #如果这里运行了5次,证明全部都是数字,已经存储到列表中
            b=b+1
    if b==5:
        #输入正确
        print("输入正确")
        break
    else:
        print("输入不正确,提示重新输入")

print(mylist2)


# a=input("请输入一个5位数字:")#123a4
# mylist2=[]
# for i in a:
#     #判断是否是数字,如果是数字就存储到列表中
#     if i.isdigit():
#         #存储到列表中
#         mylist2.append(int(i))
#
# print(mylist2)


