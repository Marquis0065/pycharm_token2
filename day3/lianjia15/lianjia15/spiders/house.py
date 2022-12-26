import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule



class HouseSpider(CrawlSpider):
    name = 'house'
    allowed_domains = ['sz.lianjia.com']
    start_urls = ['https://sz.lianjia.com/zufang/futianqu/pg1rt200600000001l1/#contentList']

    rules = (
        Rule(LinkExtractor(allow=r'pg\d+rt200600000001l1/#contentList'),
             callback='parse_item',
             follow=False),
    )

    def parse_item(self, response):
        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
        price_list = response.xpath('//em/text()')


        print(price_list.extract())





        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
