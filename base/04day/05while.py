#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
n=100
sum=0
c=1
while c<=n:
    sum=sum+c
    c+=1

print("1到100的和:",sum)

c1=0
while c1<=5:
    print(c1,"小于5")
    c1+=1
else:
    print(c1,'大于5')

# 案例:统计1-100之间包含的偶数个数,用while..else
#怎么把1-100的数打印出来
#怎么判断数是偶数
m=1
n=0
while m<=100:
    if m%2==0:
        n=n+1#5

    m=m+1
else:
    print("退出while循环后:n=",n)
# 案例:使用while嵌套循环打印如下图形
# *
# * *
# * * *
# * * * *
# * * * * *
i=0
#外循环
while i<5:#i=3
    j=0
    #内循环
    while j<=i:#j=0
        print("*",end="")#打印不换行
        j=j+1

    i=i+1
    print()#换行


'''
*
**
***



'''
# 案例:编写代码模拟用户登陆。要求：用户名为 python，密码 123456，如果输入正确，
# 打印“欢迎光临”，程序结束，如果输入错误，提示用户输入错误并重新输入,要用到break
usr='python'
pas='123456'
while True:
    user_name=input("请输入用户名:")
    user_passwd=input("请输入密码:")

    #验证用户输入的用户名和密码是否正确
    if user_name==usr and user_passwd==pas:
        print("欢迎光临")
        break#跳出循环
    else:
        print("输入错误,请重新输入")