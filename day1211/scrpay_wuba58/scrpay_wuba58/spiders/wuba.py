import scrapy


class WubaSpider(scrapy.Spider):
    name = 'wuba'
    allowed_domains = ['sz.58.com']
    start_urls = ['http://sz.58.com/']

    def parse(self, response):
        print('=============================================')
        print(response.text)
