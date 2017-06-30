# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.utils.response import get_base_url
from scrapy.utils.log import configure_logging
import logging
from wenhao.items import WenhaoItem
import sys
import string

configure_logging(install_root_handler=False)
logging.basicConfig(
    filename='log.txt',
    format='%(levelname)s: %(message)s',
    level=logging.INFO
)

f_handler = open('output.json', 'w') #将打印信息输出在相应的位置下
sys.stdout = f_handler 

add = 0
class WenhaoOne(CrawlSpider):

    name = "wen-spider"
    allowed_domains = ["cnblogs.com"]
    start_urls = [
        "http://www.cnblogs.com/whuper/default.html?page=1",
    ]

    
    # 提取匹配 whuper/default.html\?page\=([\w]+) 的链接并跟进链接(没有callback意味着follow默认为True)
    rules = (
        Rule(LinkExtractor(allow=('whuper/default.html\?page\=\d{1,}')),
                follow=True,
                callback='parse_list'
            ),
        # 提取匹配 'whuper/p/' 的链接并使用spider的parse_item方法进行分析
        #Rule(LinkExtractor(allow=('whuper/p/', )), callback='parse_item'),
    )
    #logger = logging.getLogger()

    def parse_list(self, response):
       	items = []
        sel = Selector(response)
        base_url = get_base_url(response)
        self.logger.info('###A response from %s just arrived!' % response.url) 

        postTitle = sel.css('div.day div.postTitle')
	postCon = sel.css('div.postCon')
        for index in range(len(postTitle)):
            item = WenhaoItem()
            item['title'] = postTitle[index].css("a").xpath('text()').extract()[0] 
	    item['url'] = postTitle[index].css('a').xpath('@href').extract()[0]
            #print item['listUrl']
            #print('there is no desc' + item['title'])
            try:
	        item['description'] = postCon[index].css("div.c_b_p_desc").xpath('text()').extract()[0]
            except:
                print('there is no desc')

            items.append(item)
        return items

    def parse_item(self, response):
        global add #用于统计博文的数量
        
        self.logger.info('###A response from %s just arrived!' % response.url) 

        #print  add
        add+=1
        
        sel = Selector(response)
        items = []

        item = Website()
        item['title'] = sel.xpath('/html/head/title/text()').extract()[0] #观察网页对应得html源码
        #item['description'] = sel.xpath('/html/head/title/text()').extract()#观察网页对应得html源码
        item['url'] = get_base_url(response)
        #print item
        items.append(item)
        return items

