#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
dict1 = {"name":"jbb","sex":"man","age":18}
copydi=dict1.copy()
print(copydi)
seq=[1,2,3,4]
dd={}
dd=dd.fromkeys(seq,66)
print(dd)
print(dict1.get('name2','xxx'))#如果name2没有,那么返回第二个参数
print(dict1.items())
# 案例:
# 1、逐一显示指定字典中的所有键，并在显示结束之后输出总键数
# d1={1:'a',2:'b',3:'c'}
# list1=d1.keys()
# print(list1)
# n=0
# for i in list1:
#     print(i)
#     n=n+1
# else:
#     print(n)

#
# 2、	list1 = [1,2,3,4,5,6,7],
# 	list2 = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
# 	以list1中的元素作为key，以list2中的元素作为value生成一个新的字典dict2。

list1 = [1,2,3,4,5,6,7]
list2 = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
dict2={}
for i in range(list1[0],len(list1)+1):
    dict2[i]=list2[i-1]

print(dict2)