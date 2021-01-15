#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import xlrd

def read_Exce(path,index):
    #打开xls文件
    ex=xlrd.open_workbook(path)
    sh=ex.sheets()[index]#获取第index页数的子表,
    return sh#返回的是子表中的所有内容

#第一个参数是文件名,第二个参数是文件中的第几个子表
mysh=read_Exce('aa.xls',0)
#把内容打印
for i in range(0,mysh.nrows):#mysh.nrows得到多少行
    rows=mysh.row_values(i)#得到一行数据,以列表形式返回
    print(rows)

'''
# pip install xlrd  要下载xlrd模块,pycharm下面终端输入,管理员身份打开pycharm
要引入import xlrd
'''


