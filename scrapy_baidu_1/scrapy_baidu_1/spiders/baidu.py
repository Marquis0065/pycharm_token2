import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['http://www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        print('测试爬虫scrapy程序是否正常。。。')
