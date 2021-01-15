#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
class Maker():

    def test(self):
        pass

m=Maker()
m.test()#当调用成员函数时,Python解释器会把m传递给test函数中的self参数

m1=Maker()
m1.test()


class Maker2():
    name=18

    def test(self):
        return self.name


m2=Maker2()
print("m2=",m2.test())
#定义普通函数
def mytest(age):
    a=age

#print(age),因为age是局部变量

class Maker4():
    name=18

    def test(self,age):
        self.age=age#self.age是对象属性,self是区分局部变量和对象属性
        return self.age

    def test02(self):
        print(self.age)

m4=Maker4()
m4.test(88)
print(m4.age)
m4.score=20#对象属性
print(m4.score)

m4.test02()

# m5=Maker4()
# m5.test02()
print("----------------")
class Maker5():
    name='小明'

    # def test(self):
    #     self.name='小花'#有这行,那么打印的是小花,没有这行打印的是小明
    #     return self.name

    def test02(self,name):
        return self.name#区分局部变量name和类变量name

m5=Maker5()
print(m5.test02('小星'))

# m6=Maker5()
# print(m6.name)
print("--------------")
class Maker22():
    name = 18  # 类变量


    def test(self):
        self.name = 38
        return self.name

m22 = Maker22()
print(m22.test())  # 38
m88 = Maker22()
print(m88.name)  # 18

class Maker33():
		def test(self):
			self.score=88#在成员函数中定义对象属性

m33=Maker33()
m33.test()
print(m33.score)


# 案例:有对象属性(姓名,年龄,分数),设计一个类,类中有修改对象属性值的方法,打印对象属性的方法
# 其中分数属性在修改函数内定义,修改年龄时要判断是否合法,如果不合法打印不合法
class Maker():
    # def createScore(self):  # 创建对象属性的方法
    #     self.score = 99

    # def setName(self, Name):  # 修改对象属性的方法
    #     self.name = Name
    #
    # def printName(self):  # 打印对象属性的方法
    #     print(self.name)
    #
    # def setAge(self,age):#设置年龄的方法
    #     if age>0 and age<140:
    #         self.age=age
    #     else:
    #         print("输入的年龄不合法")
    #
    # def printAge(self):#打印年龄的方法
    #     print(self.age)

    def setScore(self,score):#设置分数的方法
        self.score=score#创建对象属性并赋值

    def printScore(self):#打印分数的方法
        print(self.score)

m = Maker()
# m.name = 'aa'
# m.age = 18
# # m.createScore()
# # print('score=',m.score)
#
# print(m.name)  # aa
# m.setName('bb')
# m.printName()  # bb
# print("-----------")
# print(m.age)#18
# m.setAge(100)
# m.printAge()#88
print("-----------")

m.setScore(199)
print(m.score)#
m.printScore()

