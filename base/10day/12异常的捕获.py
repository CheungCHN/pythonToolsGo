#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
# print(a)

# try:
#     print("111111")
#     print(a)
# except Exception as e:
#     print(e)
# else:
#     print("没有异常")
# finally:
#     print("有没有异常都要执行我")
# def test():
#     print("test")
# test()
# input(".....")

def test():
    try:
        print(1/0)
    except Exception as e:
        raise #抛出异常

# test()

def test02():
    try:
        test()
    except Exception as e:
        print(e)



test02()
#
# input("ssss:")
