#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Parent:        # 定义父类
   parentAttr = 100
   def __init__(self):
      print "paerents init"

   def parentMethod(self):
      print 'paerents parentMethod000000000000'

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print "paerents_attr :", Parent.parentAttr

class Child(Parent): # 定义子类
   def __init__(self):
      print "son __init__"

   def childMethod(self):
    #在类中调用父方法,加前缀
      Parent.parentMethod(self);
      print 'son child method'

c = Child()          # 实例化子类
c.childMethod()      # 调用子类的方法
c.parentMethod()     # 调用父类方法

c.setAttr(200)       # 再次调用父类的方法
c.getAttr()          # 再次调用父类的方法
