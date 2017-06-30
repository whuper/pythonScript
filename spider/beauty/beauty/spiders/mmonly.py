# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
#from scrapy.utils.response import get_base_url

class MmonlySpider(scrapy.Spider):
    name = "mmonly"
    allowed_domains = ["mmonly.com"]
    start_urls = (
        'http://www.mmonly.cc/tag/xh1/1.html',
    )
     # 提取匹配  的链接并跟进链接(没有callback意味着follow默认为True)
    rules = (
        Rule(LinkExtractor(allow=('tag/xh1/\d{1,}.html')),
                follow=True,
                callback='parse_list'
            ),
        # 提取匹配 'whuper/p/' 的链接并使用spider的parse_item方法进行分析
        #Rule(LinkExtractor(allow=('whuper/p/', )), callback='parse_item'),
    )

    def parse_list(self, response):
       	items = []
        sel = Selector(response)
        #base_url = get_base_url(response)
        self.logger.info('###A response from %s just arrived!' % response.url) 

        postTitle = sel.css('div.day div.postTitle')
	postCon = sel.css('div.postCon')
        for index in range(len(postTitle)):
            item = Website()
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
