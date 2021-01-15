#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
mylist=[1,2,3,4,5,'a','b','a']
mylist.remove(2)
print(mylist)
mylist.remove('a')
print(mylist)

#案例:给定一个列表，首先删除以s开头的元素，删除后，修改第一个元素为"maker"，并且并且把最后一个元素复制一份，放在maker的后边
#假如有列表['str1','look','one','student','black','aaa']
my_list=['str1','look','one','student','black','aaa']
for i in my_list:
    if i.startswith('s'):
        my_list.remove(i)
print(my_list)

my_list[0]='maker'
print(my_list)
my=my_list[-1]
print(my)
my_list.insert(1,my)
print(my_list)