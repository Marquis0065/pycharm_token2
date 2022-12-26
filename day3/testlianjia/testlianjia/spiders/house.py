import scrapy


class HouseSpider(scrapy.Spider):
    name = 'house'
    allowed_domains = ['sz.lianjia.com']

    start_urls = ['https://sz.lianjia.com/zufang/futianqu/pg1rt200600000001l1/#contentList']

    def parse(self, response):
            print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
            price = response.xpath('//em/text()').extract()
            print(price)
            print(response.xpath('//em/text()').extract_first())

