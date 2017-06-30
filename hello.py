#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time;
import calendar
#raw_input("\n\nPress the enter key to exit.")
counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串

print counter
print miles
print name
print ("hello,wenhao");

#List列表
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print list # 输出完整列表
print list[0] # 输出列表的第一个元素
print list[1:3] # 输出第二个至第三个的元素 
print list[2:] # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2 # 输出列表两次
print list + tinylist # 打印组合的列表


#元字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象结合，字典是无序的对象集合。
#两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
#字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print dict['one'] # 输出键为'one' 的值
print dict[2] # 输出键为 2 的值
print tinydict # 输出完整的字典
print tinydict.keys() # 输出所有键
print tinydict.values() # 输出所有值

#元组是另一个数据类型，类似于List（列表）。
#元组用"()"标识。内部元素用逗号隔开。但是元素不能二次赋值，相当于只读列表。
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')

var = 100 
 
if ( var  == 100 ) : print "变量 var 的值为100" 
 
print "Good bye!" 

#var = 1
#while var == 1 :  # 该条件永远为true，循环将无限执行下去
   #num = raw_input("Enter a number  :")
   #print "You entered: ", num
for letter in 'Python':     # 第一个实例
   print '当前字母 :', letter

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print '当前字母 :', fruit

print "Good bye!"

# 定义函数
def printme( str ):
#   "打印任何传入的字符串"
   print str;
   return;
 
printme("i am a lazy dog");

total = 11; # 这是一个全局变量
# 可写函数说明
def sum( arg1, arg2 ):
   #返回2个参数的和."
   #total = arg1 + arg2; # total在这里是局部变量.
   print "函数内是局部变量 : ", total
   return total;
 
#调用sum函数
sum( 10, 20 );
print "函数外是全局变量 : ", total

Money = 2000
def AddMoney():
   # 想改正代码就取消以下注释:
   global Money
   Money = Money + 1
 
print Money
AddMoney()
print Money

var1 = 'Hello World!'
print "Updated String :- ", var1[:6]+'Python','good'
print "My name is %s and weight is %d kg!" % ('Zara', 51)

print time.time();
localtime =  time.strftime('%Y-%m-%d %H:%I:%S',time.localtime(time.time()) )
year =  int( time.strftime('%Y',time.localtime(time.time()) ) )
month =  int( time.strftime('%m',time.localtime(time.time()) ) )
localtime =  time.strftime('%Y-%m-%d %H:%I:%S',time.localtime(time.time()) )
print "Local current time :", localtime

print year
print month
#cal = calendar.month(year, month)
#print "Here is the calendar:"
#print cal;

# 打开一个文件
fo = open("foo.txt", "wb")
#fo.write( "Python is a great language.\nYeah its great!!\n我想我快要下班了");
 
# 关闭打开的文件
fo.close()


class Employee:
   '所有员工的基类'
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
