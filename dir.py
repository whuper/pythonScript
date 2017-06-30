#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
fo = open("dir.txt", "wb")
dir_list = []

for i in os.listdir('.'):
    if os.path.isdir(i):
        dir_list.append(i + '\n')

#writelines() 方法用于向文件中写入一序列的字符串。
fo.writelines(dir_list);
print dir_list
fo.close()
