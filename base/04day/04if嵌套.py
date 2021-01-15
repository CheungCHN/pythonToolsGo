#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
a=10
b=20
if a<b:

   if a>15:
       print("a>15")
   elif a<15:
       print("a<15")
   else:
       print("a=15")

   print("if结束")
elif a>b:
    print('a>b')
else:
    print('a=b')


#案例:从终端输入,用户名,密码用户身份验证: 用户名输入admin, 密码输入123456, 验证成功,用嵌套的方法
# x=input("请输入用户名:")
#
# if x=='admin':
#
#     y = input("请输入密码:")
#     if y=='123456':
#         print("验证成功")
#     else:
#         print("输入的密码不正确")
#
# else:
#     print("输入的用户名不正确")

#案例,猜数字,有一个数字,389,猜中第一位才可以继续往下猜,没猜中就现在'很遗憾,没猜中',猜中了就现在
#'恭喜你,猜中了,请继续',全猜中,打印'太棒了,全中'
m=int(input("请输入第一个数字:"))
if m==3:

    print('恭喜你,猜中了,请继续')
    m = int(input("请输入第二个数字:"))

    if m==8:

        print('恭喜你,猜中了,请继续')
        m = int(input("请输入第三个数字:"))
        if m==9:
            print('太棒了,全中')
        else:
            print("很遗憾,没猜中")

    else:
        print("很遗憾,没猜中")

else:
    print("很遗憾,没猜中")
