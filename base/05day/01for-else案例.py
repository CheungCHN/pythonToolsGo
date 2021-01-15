#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

#案例:输出10-20之间的素数
#说明:质数又称素数。一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数叫做质数
#这个数,除1可以得到整的,除自己可以得到整的,除其他得不到整的,有余数
#如11,13,17,19
for i in range(10,21):
    for x in range(2,i):
        if i%x==0:
            break
    else:
        print(i)




#案例:统计100以内能够被2整除，但是不能被3整除的数的个数
cc=0
for i in range(101):
    if not i%2 and i%3:
        cc+=1
else:
    print("cc=",cc)



