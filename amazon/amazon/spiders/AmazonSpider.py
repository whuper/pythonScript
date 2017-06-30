# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.utils.response import get_base_url
from scrapy.utils.log import configure_logging
import sys
import string
import logging

from amazon.items import AmazonItem

configure_logging(install_root_handler=False)
logging.basicConfig(
    filename='log.txt',
    format='%(levelname)s: %(message)s',
    level=logging.INFO
)

class AmazonSpider(Spider):
    name = 'amazon'#唯一标识spider的名字 最后用scrapy crawl + name的值来运行爬虫
    allowed_domains = ["amazon.cn"]
#上面复制的URL集合用在此处，初始地址

    start_urls = [
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3AHuawei%20%E5%8D%8E%E4%B8%BA',
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3A%E9%AD%85%E6%97%8F', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3ANokia%20%E8%AF%BA%E5%9F%BA%E4%BA%9A', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3ASamsung%20%E4%B8%89%E6%98%9F', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3ACoolpad%20%E9%85%B7%E6%B4%BE', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3ALenovo%20%E8%81%94%E6%83%B3', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3AApple', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3A%E5%B0%8F%E7%B1%B3', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3AASUS%20%E5%8D%8E%E7%A1%95', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3AHTC', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3ASony%20%E7%B4%A2%E5%B0%BC', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3APhilips%20%E9%A3%9E%E5%88%A9%E6%B5%A6', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3A21%E5%85%8B%E6%89%8B%E6%9C%BA', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3AZTE%20%E4%B8%AD%E5%85%B4', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3ABIRD%20%E6%B3%A2%E5%AF%BC', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3ANewsmy%20%sE7%BA%BD%E6%9B%BC', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3ATCL',
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3AMicrosoft%20%E5%BE%AE%E8%BD%AF', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3A%E5%8A%AA%E6%AF%94%E4%BA%9A', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3ASOYES', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3A%E7%BE%8E%E5%9B%BE', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3A%E7%88%B1%E6%B4%BE%E5%B0%94', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3A%E7%99%BE%E5%8A%A0', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3ADazen%20%E5%A4%A7%E7%A5%9E', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3A%E4%B8%80%E5%8A%A0', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3A%E9%94%8B%E8%BE%BE%E9%80%9A', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3ABlackBerry%20%E9%BB%91%E8%8E%93', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3A%E9%87%91%E6%9D%A5', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3A%E8%8D%A3%E7%83%BD', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3A%E5%A4%A7%E6%98%BE', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3AGIONEE%20%E9%87%91%E7%AB%8B', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3AMANN', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3A%E6%AF%94%E9%85%B7', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3ASmartisan%20%E9%94%A4%E5%AD%90', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3A%E7%83%BD%E7%81%AB', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3AKonka%20%E5%BA%B7%E4%BD%B3', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3Avivo', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3A%E4%B8%B0%E5%87%AF%E8%BE%BE', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3A%E7%A7%BB%E5%8A%A8', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3A%E8%89%BE%E5%B0%94%E9%85%B7', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3AMelrose', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3A%E9%94%90%E6%97%8F', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3A%E6%B3%A2%E5%AF%BC', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3AM%C2%B7PARTY', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3AHaier%20%E6%B5%B7%E5%B0%94', 
            'http://www.amazon.cn/s?ie=UTF8&page=1&rh=n%3A665002051%2Cp_4%3AMeitu%20%E7%BE%8E%E5%9B%BE' 
            ]

    #处理response
    def parse(self,response):
        #self.logger.info('@@@@5555@@@@@')
        #在处理response传来的页面时，先判断有无下一页，有的话链接加到URL的集合里面
        """
        NextPage = response.xpath("//a[@id='pagnNextLink']/@href").extract()
        if(NextPage !=[]): 
            self.start_urls.append('http://www.amazon.cn' + NextPage[0])
        """
        
        logger = logging.getLogger()
        #sites是每个手机商品的那个li块儿
        sel = Selector(response)
        sites = sel.xpath('//ul[@class="s-result-list"]/li[@class="s-result-item"]')
        #sites = response.xpath('//ul[@class="s-result-list"]/li[@class="s-result-item"]')
        #sites = sel.xpath('//div[@id="news_list"]/div[@class="news_block"]')
        #分别对每个手机商品的信息进行处理
        items = []
        for site in sites:
            self.logger.info('@@@@99999@@@@@')
            Yamaxun = AmazonItem() 
            Yamaxun['price'] = site.xpath("div/div[3]/div[1]/a/span/text()").extract() #手机价格
            Yamaxun['description'] = site.xpath("div/div[2]/div[1]/a/h2/text()").extract()#信息
            Yamaxun['URL'] = site.xpath("div/div[2]/div[1]/a/@href").extract()
            Yamaxun['Photo'] = site.xpath("div/div[1]/div/div/a/img/@src").extract()
            items.append(Yamaxun)

            self.logger.info('###########A response from %s just arriveda####################') 

            logger.info('@@@@@@@@@@@@@@@@@@@')

         # info('parsed ' + str(response)) 
        return items
