#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb

class Employee:
   #所有员工的基类
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount


class Parent:        # 定义父类
   def myMethod(self):
      print 'parents parents'

class Child(Parent): # 定义子类
   def myMethod(self):
      print 'son son'

c = Child()          # 子类实例
c.myMethod()         # 子类调用重写方法


class JustCounter:
	__secretCount = 0  # 私有变量
	publicCount = 0    # 公开变量

	def count(self):
		self.__secretCount += 1
		self.publicCount += 1
		print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()
print counter.publicCount
#print counter.__secretCount  # 报错，实例不能访问私有变量
print counter._JustCounter__secretCount
