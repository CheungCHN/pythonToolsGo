#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
class Father():
    def test(self):
        print("我有加法功能")

class Son(Father):
    def test(self):
        print("我有加减乘除的功能")
s=Son()
s.test()


