#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
ss={1,2,3,4}
ss.remove(2)
print(ss)
ss.discard(3)
print(ss)
ss.pop()
print(ss)
s={'hello','wo','ld','aaa'}
s.pop()
print(s)
del ss
#print(ss)
s2={1,'aa','bb',2,3}
s2.pop()
print(s2)
#案例:有集合{1,2,3,'hello','world'},删除全部字符串,然后删除最左边第一个元素
s3={1,2,3,'hello','world'}
s3.discard('hello')
s3.discard('world')
print(s3)
s3.pop()
print(s3)




