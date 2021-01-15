#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
#创建列表
mylist=[]
mylist2=[1,'a','qianfeng',20.22]
print(mylist2[0])
#修改元素和访问元素
#mylist[0]=66 报错
mylist2[0]=88
print(mylist2)
print(mylist2[1:2])
dd=mylist+mylist2
print(dd)
#列表里的元素是列表
mylist3=[1,[1,2,3],20.22,['a','b']]
print(mylist3)
print(mylist3[1][1])
print("-----------------")
#案例:通过循环的方式打印出list列表中的元素
list=[1,2,3,4,5]
for i in list:
    print(i)
#案例:有列表my=[1,2,3,4,5],把列表变为[10,20,30,40,50]
my=[1,2,3,4,5]
# for i in my:
#     my[i-1]=i*10
# print(my)

# for i in range(5):
#     my[i]=my[i]*10
# print(my)


my=[1,2,3,4,5]
my[0:5]=10,20,30,40,50
print(my)
#案例:有列表my2=[1,2,'a',3,'b',4],把列表中的字母a变为前面的数字之和,把b变为前面数字之和
#最后计算整个列表的数字之和.假设字母位置不固定，字母的个数也不固定（有难度）
#1.循环列表中的元素,判断哪个元素是字母
#2.
my2=[1,2,'a',3,'b']
d=0#标志下标
s=0#记录整个列表之和
for i in my2:
    print('i=',i,' d=',d)
    if type(i)==str:#str==str
        for j in range(d):
            if j==0:#先把my2中的a变为0,方便下面进行加法
                my2[d]=0  #my2=[1,2,0,3,'b',4]
            my2[d]=my2[d]+my2[j] #    =1+2    my2=[1,2,3,3,'b',4]
        i=my2[d]#累加整个列表之和时,为了避免整数加字符串
    s+=i
    d=d+1


print(my2)
print(s)

