#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
str='abcdefg'
print(str)
print(str[0:2])
print(str[0:-1])#从第一个字符打印到倒数第二个字符
print(str[2:])#从第三个字符打印到最后一个字符
print(str[1:-6])#如果没有区间就不打印
print(str[:3])#abc.从第一个字符打印到第三个字符
print(str[::2])#从左往右打印,跳跃1个字符
print(str[::-2])#从右往左打印,跳跃1个字符
#因为str[5:1]区间是cdef
#步长是负数,那么从右往左,
print(str[5:1:-2])#fd,

#案例:给定一个字符串aStr,请反转它
s='aStr'
print(s[::-1])
#案例:有字符串'123456789',打印单数出来
s2='123456789'
print(s2[::2])
#案例:有字符串'hello world 123 abc',打印出world和abc
s3='hello world 123 abc'
print(s3[6:11])
print(s3[16:19])
print(s3[-3:])
print(s3[5:1:2])#不会打印


