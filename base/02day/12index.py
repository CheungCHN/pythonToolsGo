#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
str='helloworld'

print(str.index('ll'))
#案例:有字符串'百度,华为,腾讯,阿里,华子,京东,美图秀秀',查询是否有华子.然后截取出华子来,打印出来
str2='百度,华为,腾讯,阿里,华子,京东,美图秀秀'
print(str2.index('华子'))
n=str2.index('华子')
print(str2[n:n+2])



