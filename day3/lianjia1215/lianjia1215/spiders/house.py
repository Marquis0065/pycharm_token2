import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from lianjia1215.items import Lianjia1215Item


class HouseSpider(CrawlSpider):
    name = 'house'
    allowed_domains = ['sz.lianjia.com']
    start_urls = ['https://sz.lianjia.com/zufang/longhuaqu/pg2rt200600000001l1/']

    rules = (
        Rule(LinkExtractor(allow=r'/longhuaqu/pg\d+rt200600000001l1/'),
             callback='parse_item',
             follow=False),
    )

    def parse_item(self, response):
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
        price_list = response.xpath('//em/text()')

        price1 = price_list.extract()
        print(price1)
        price=Lianjia1215Item(price=price1)
        yield price

        print('*******************太平洋汽车********************************')

