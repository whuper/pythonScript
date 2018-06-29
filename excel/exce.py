# -*- coding: UTF-8 -*-

import xlrd
import json

workbook = xlrd.open_workbook(u'./file.xlsx')

sheet_names = workbook.sheet_names()

print(u'就看到静安寺框架')
def store(data):
    with open('data.json','w') as json_file:
        json_file.write(json.dumps(data))

list = []


for sheet_name in sheet_names:
    sheet = workbook.sheet_by_name(sheet_name)
    cols = sheet.col_values(0) # 获取第二列内容
    #print cols
    print type(cols[0])  
    #store(cols)



