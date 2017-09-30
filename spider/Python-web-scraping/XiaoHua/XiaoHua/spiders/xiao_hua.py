# --coding:utf-8--
import scrapy
from XiaoHua.items import XiaohuaItem
from scrapy.http import Request
import requests
import re
import os
import sys
reload(sys)

sys.setdefaultencoding('utf-8')

class XiaoHua(scrapy.Spider):
    name='XiaoHua'
    allowed_domains=['mmonly.cc']
    base=r'E:/beauties/'
    def start_requests(self):
        #一共有6页
        '''
        for i in range(1,7):
            url='http://www.mmonly.cc/tag/xh1/'+str(i)+'.html'
            yield Request(url,callback=self.parse_one)
        '''
        url='http://www.mmonly.cc/tag/xh1/1.html'
        yield Request(url,callback=self.parse_one)


    def parse_one(self,response):
        #创建一个大的list存储所有的item
        items=[]
        #pattern=re.compile(r'<div class="title".*?<a.*?href="(.*?)">(.*?)</a></span></div>',re.S)
        #mains=re.findall(pattern,response.text)
        mains=response.css("div.title")
        for main in mains:
            #创建实例,并转化为字典
            item=XiaohuaItem()
            item['siteURL']=main.css("span > a::attr(href)").extract_first()
            item['title']=main.css("span > a::text").extract_first()
            try:
                item['fileName']=self.base+item['title']
            except:
                item['title']=main.css("span > a > b::text").extract_first()
                item['fileName']=self.base+item['title']
            items.append(item)

        for item in items:
            #创建文件夹
            fileName=item['fileName']
            if not os.path.exists(fileName):
                os.makedirs(fileName)
            #用meta传入下一层
            yield Request(url=item['siteURL'],meta={'item1':item},callback=self.parse_two)

    def parse_two(self,response):
        #传入上面的item1
        item2=response.meta['item1']
        source=requests.get(response.url)
        html=source.text.encode('utf-8')
        pattern=re.compile(r'共(.*?)页',re.S)
        Num=re.search(pattern,html).group(1)
        items=[]
        for i in range(1,int(Num)+1):
            item=XiaohuaItem()
            item['fileName']=item2['fileName']
            #构造每一个图片的存储路径
            item['path']=item['fileName']+'/'+str(i)+'.jpg'
            #构造每一个图片入口链接，以获取源码中的原图链接
            item['pageURL']=response.url[:-5]+'_'+str(i)+'.html'
            items.append(item)
        for item in items:
            yield Request(url=item['pageURL'],meta={'item2':item},callback=self.parse_three)

    def parse_three(self,response):
        item=XiaohuaItem()
        #传入上面的item2
        item3=response.meta['item2']
        #pattern=re.compile(r'<li class="pic-down h-pic-down"><a target="_blank" class="down-btn" href=\'(.*?)\'>.*?</a>',re.S)
        #URL=re.search(pattern,response.text).group(1)
        URL=response.css("li.pic-down > a.down-btn::attr(href)").extract_first()
        item['detailURL']=URL
        item['path']=item3['path']
        item['fileName']=item3['fileName']
        yield item










