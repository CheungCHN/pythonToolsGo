#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
a=1
while True:
    if a>5:
        print("退出循环")
        break
    print("a=",a)
    a+=1

for i in range(5):
    if i==3:
        break
    print("i=",i)

for i in range(5):
    if i==3:
        continue
    print(i+1)
print("----------")

b=1
while True:
    if b==2:
        for i in range(b):
            print("i=",i)#0
            break

    b=b+1
    print("b=",b)#2 3
    if b==3:
        break




#案例:实时监控用户的输入,当用户输入66时,退出
# while True:
#     n=int(input("请输入一个数字:"))
#     if n==66:
#         break

#案例:猜数字游戏，猜到比确定数字大的显示大了，小的显示小了，重新输入，才中了退出
a=88
while True:
    e=int(input("请输入一个数字:"))
    if e<a:
        print("小了")
    elif e>a:
        print("大了")
    else:
        print("猜对")
        break