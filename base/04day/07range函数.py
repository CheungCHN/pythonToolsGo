#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
for i in range(5):
    print(i)

print("-------------")
for i in range(3,8):
    print(i)

# for i in range('12345'):
#     print(i)
print("------------")
a=10
for i in range(a):
    print(i)
print("------------")

for i in range(3,8,3):
    print(i)
print("------------")
for i in range(20,10,-2):
    print(i)
#注意:如果步长是负数,那么区间要从大到小
print("------------")
#案例:用for加range()函数输出10-20的偶数,反向打印
for i in range(20,9,-2):
    print(i)
#案例:打印以下图形
# 0123456789
# 10112131415
# 1617181920
for i in range(21):
    if i<10:
        print(i,end="")
    if i==10:
        print()
    if i>=10 and i<=15:
        print(i,end="")
    if i==16:
        print()
    if i>=16 and i<=20:
        print(i,end="")