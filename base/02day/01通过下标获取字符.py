#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
str="abcdef"
a=str[0]
b=str[1]
print("a=%s,b=%s"%(a,b))
str2="中国在亚洲"
print(str2[0])#中
print(str2[2])#在
#获取str字符串中最后一个字符
print(str[5])
str3='fadsfasdfasdfasdfsa1234324dad'
print(str3[-2])
#print(str[6])越界报错

#案例:定义一个变量,变量赋值'中华人民共和国',取出中国来分别赋值给a,b变量,并打印出来
str='中华人民共和国'
a1=str[0]
b1=str[-1]
print(a1,b1)

#案例:有字符串str='北京,上海,广州,深圳的房价都很高,但是咸鱼都有梦想,
# 超市冷藏柜的50元螃蟹都知道往100元一斤的柜子爬,我们呢?加油!梦想在不远的地方,面包就在眼前!',
# 请从上述字符串获取字符组成'我们在深圳,有100的梦想',打印出来
mystr='北京,上海,广州,深圳的房价都很高,但是咸鱼都有梦想,\
超市冷藏柜的50元螃蟹都知道往100元一斤的柜子爬,我们呢?加油!梦想在不远的地方,面包就在眼前!'
print(mystr)
m1=mystr[-23]
m2=mystr[-22]
m3=mystr[-4]
m4=mystr[9]
m5=mystr[10]
m6=mystr[-8]
m7=mystr[23]
m9=mystr[-34]
m10=mystr[-33]
m11=mystr[-32]
m12=mystr[-11]
m13=mystr[24]
m14=mystr[25]
print(m1,m2,m3,m4,m5,m6,m7,m9,m10,m11,m12,m13,m14)