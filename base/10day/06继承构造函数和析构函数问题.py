#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
#如果子类没有写构造函数,那么使用父类的构造函数
class Father():
    def __init__(self):
        print('我是父类的构造函数')

class Son(Father):
    pass

s=Son()

#如果子类有自己的构造函数,那么调用自己的构造函数
class Son2(Father):
    def __init__(self):
        print("我是Son2的构造函数")

s2=Son2()
print("----------")
#如果子类写了自己的构造函数,还要使用父类的构造函数
class Son3(Father):
    def __init__(self):
        #调用父类的构造函数
        super(Son3,self).__init__()
        #调用父类的构造函数
        Father.__init__(self)
        print("我是Son3的构造函数")

s3=Son3()

print("================")
#案例:测试一下析构函数是怎么样的?
#如果子类没有写析构函数,那么使用父类的析构函数
class FatherX():
    def __del__(self):
        print('我是父类的析构函数')

# class SonX(FatherX):
#     pass
#
# sX=SonX()
#
# #如果子类有自己的析构函数,那么调用自己的析构函数
# class Son2X(FatherX):
#     def __del__(self):
#         print("我是Son2的析构函数")
#
# s2X=Son2X()
print('------------2-----------')
#如果子类写了自己的析构函数,还要使用父类的析构函数
class Son3X(FatherX):
    def __del__(self):
        #调用父类的析构函数
        super(Son3X,self).__del__()
        #调用父类的析构函数
        FatherX.__del__(self)
        print("我是Son3的析构函数")

s3X=Son3X()

def test():
    ss=Son3X()

test()
print("------3----------")

input("sssssss:")

