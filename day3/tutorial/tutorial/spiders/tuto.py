import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tutorial.items import TutorialItem


class TutoSpider(CrawlSpider):
    name = 'tuto'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/page/1/']

    rules = (
        Rule(LinkExtractor(allow=r'/page/\d+\/'),
             callback='parse_item',
             follow=True),
    )

    def parse_item(self, response):
        # item = {}
        # #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # #item['name'] = response.xpath('//div[@id="name"]').get()
        # #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
        print('***********************名人名言******************')
        text_list = response.xpath('//div[@class="quote"]/span[1]/text()')

        content = text_list.extract()
        print(content)
        quote = TutorialItem(quote = content)
        yield quote
