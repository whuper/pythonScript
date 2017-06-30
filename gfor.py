#!/usr/bin/python
# -*- coding: UTF-8 -*-
sample_url = 'http://my.cdn.tokyo-hot.com/samples/'
fo = open("toky-hot-samples.txt", "wb")
url_list = []
for num in range(1125,1236):  # 迭代 10 到 20 之间的数字
    str_num = 'n' + str(num)
    mp4_url = sample_url + str_num + '.mp4'
    #fo.write(mp4_url + '\n');
    url_list.append(mp4_url + '\n')
    #print mp4_url
#writelines() 方法用于向文件中写入一序列的字符串。
fo.writelines(url_list);
print url_list
fo.close()
