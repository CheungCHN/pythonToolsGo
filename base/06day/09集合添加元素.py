#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
s={1,2,3,4}
s.add(8)
s.add("world")
print(s)
s.update([9,10])
s.update('hello')
print(s)

#案例:从终端输入一个数字就加入集合中,然后打印,又输入一个数字,然后打印,直到输入-1,退出输入
#然后打印最终的集合
# s1=set()
# while 1:
#     a=int(input('请输入数字:'))
#     if a==-1:
#         break
#     s1.add(a)
#     print(s1)
# print(s1)

#案例:从终端输入一个字符串就加入集合中,然后打印,又输入一个字符串,然后打印,直到输入q,退出输入
#然后打印最终的集合,字符串要分开存储,如输入hello,存储的列表是{'h','e','l','o'}
s1=set()
while 1:
    a=input('请输入数字:')
    if a=='q':
        break
    s1.update(a)
    print(s1)
print(s1)
