#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
#自定义异常类
class ShowMy(Exception):
    def __init__(self,length,atle):
        super().__init__()#调用父类的构造函数
        self.length=length
        self.atle=atle

def main():
    try:
        s=input("请输入-->")
        if len(s)<3:
            raise ShowMy(len(s),3)
    except ShowMy as e:
        print('你输入的是:',e.length,'输入的长度要大于:',e.atle)
    else:
        print("没有异常发生")

# main()


# 案例:编写代码，提示用户输入文件名， 如果文件存在就打印文件内容，如果文件不存在，捕获异常
a=input("请输入文件名:")
try:
    f=open(a,'r')
    b=f.read()
    print(b)
except Exception as e:
    print(e)
else:
    print("没有异常")


