#!/usr/bin/python
#coding:utf-8

import urllib;
baidu = urllib.urlopen("http://www.baidu.com")
print baidu.info #输出baidu首页头部信息
print baidu.getcode() #输出baidu首页网页的状态码
print baidu.geturl() #输出请求的url地址
for line in baidu:
    print line,
baidu.close() #关闭对象方法
