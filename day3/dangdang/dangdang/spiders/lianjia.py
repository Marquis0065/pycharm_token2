import scrapy
from dangdang.items import DangdangItem


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['sz.lianjia.com']
    start_urls = ['https://sz.lianjia.com/zufang/']
    base_url = 'https://sz.lianjia.com/zufang/pg'
    #https://sz.lianjia.com/zufang/pg2/#contentList
    page = 1

    def parse(self, response):
        print('*********************************************************')
        # src = '//div[@class="content__list--item"]//a/img/@data-src'
        # name ='//div[@class="content__list--item"]/div[1]/p[2]//a[3]'
        # price = '//div[@class="content__list--item"]/div[1]/span'
        # content= response.xpath(name)

        for i in response.xpath('//div[@class="content__list--item"]'):
            src = i.xpath('.//a/img/@data-src').extract_first()
            name = i.xpath('./a/@title').extract_first()
            price = i.xpath('./div//em/text()').extract_first()
            print(src,name,price)
            book = DangdangItem(src=src, name=name, price=price)
            # 交给管道
            yield book

        if self.page<20:
            self.page = self.page+1
            url = self.base_url+str(self.page)+'/#contentList'

            #scrapy.Request 就是get请求
            yield scrapy.Request(url=url,callback=self.parse)


