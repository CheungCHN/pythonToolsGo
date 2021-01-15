#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
class Father():
	def test(self):

		print("Father test")

	def test01(self):
		print("Father test01")

class Son(Father):
    def test(self):
    	print("Son test")

    def test01(self):
       super().test01()


s=Son()
s.test()
s.test01()





