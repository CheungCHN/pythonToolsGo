#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
d={}
d1={1:'a',2:'b'}
print(d1[1])#通过键来访问对应的值
print(d1)#访问完整的字典
print(d1.keys())#输出所有的键
print(d1.values())#输出所有的值
print(d1.get(1))
#print(d1[8])#如果键不存在,去访问,那么会报错
if d1.get(8)!=None:
    pass


#案例:从终端输入,输入格式为key:value模式,如:name:maker,然后把数据存储到字典中
# str=input("请输入一对键值对:")#name:maker
# print(str)
# a=str.split(':')[0]
# b=str.split(':')[1]
# dd={a:b}
# print(dd)
#案例:有字典dict={1:'悟空',2:'短笛',3:'贝吉塔',4:'小林',5:'冰河'}
#请把字典dict的键取出,赋值给list1,把值取出,赋值给list2,再list1尾部添加66,list2尾部添加'星失'
dict={1:'悟空',2:'短笛',3:'贝吉塔',4:'小林',5:'冰河'}
list1=list(dict.keys())
print(list1)
list2=list(dict.values())
print(list2)
list1.append(66)
list2.append('星失')
print(list1)
print(list2)
print(list(dict.keys())[0])


