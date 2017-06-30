# Scrapy settings for blog project

BOT_NAME = 'blog'

CONCURRENT_REQUESTS = 200
LOG_LEVEL = 'INFO'
COOKIES_ENABLED = False
RETRY_ENABLED = True


SPIDER_MODULES = ['blog.spiders']
NEWSPIDER_MODULE = 'blog.spiders'
DEFAULT_ITEM_CLASS = 'blog.items.Website'
DOWNLOADER_MIDDLEWARES = {
        #'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
        'scrapy.downloadermiddlewares.useragent' : None,
        'blog.spiders.rotate_useragent.RotateUserAgentMiddleware' :400,
    }
#ITEM_PIPELINES = {'blog.pipelines.FilterWordsPipeline': 1}

ITEM_PIPELINES = {
    #'blog.pipelines.PricePipeline': 300,
    'blog.pipelines.JsonWriterPipeline': 800,
}
"""
FEED_EXPORTERS_BASE = {
    'json': 'scrapy.contrib.exporter.JsonItemExporter',
    'jsonlines': 'scrapy.contrib.exporter.JsonLinesItemExporter',
    'csv': 'scrapy.contrib.exporter.CsvItemExporter',
    'xml': 'scrapy.contrib.exporter.XmlItemExporter',
    'marshal': 'scrapy.contrib.exporter.MarshalItemExporter',
}
"""
