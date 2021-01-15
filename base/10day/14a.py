#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import os

'''
import os
	#   path = os.getcwd()#获取当前执行文件的绝对路径
	#   path = os.path.abspath('.')#获取当前路径
	#     # path = os.path.abspath('..')#获取当前的父路径
'''
# path=os.getcwd()
# print(path)
# a1=os.path.abspath('.')
# print(a1)
#
# a2=os.path.abspath('..')
# print(a2)

import sys
print('===Python import mode===')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

import os
funFlag = 2 # 1表示添加标志,2表示删除标志
folderName = './文件/'
#获取指定路径下所有文件的名字
dirList = os.listdir(folderName)
#遍历输出所有文件的名字
for name in dirList:
	print(name)
	if funFlag==1:
		newName='[山哥出品]-'+name
	elif funFlag==2:
		num=len('[山哥出品]-')
		newName=name[num:]
	print(newName)
	os.rename(folderName+name,folderName+newName)