# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

class AmazonPipeline(object):
#spider中的item会传递到这儿处理，这里将其写入json文件中
    def __init__(self):
        self.file = codecs.open('amazon_iPhone.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) +"\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()
