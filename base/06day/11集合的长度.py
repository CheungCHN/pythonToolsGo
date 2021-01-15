#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
s={1,2,3,4}
print(len(s))
#案例:有集合{1,2,3,4,'hello','a'},保留1个元素,其他的删除,假如元素个数不确定
s1={1,2,3,4,'hello','a'}
for i in range(len(s1)-1):
    s1.pop()
print(s1)
