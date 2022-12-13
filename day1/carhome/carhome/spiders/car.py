import scrapy


class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['www.car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/price/brand-15.html#pvareaid=3311273']

    def parse(self, response):
        print('汽车一家')
        content = response.xpath('//div[@class="main-title"]/a/text()').extract()
        price = response.xpath("//div[@class='main-lever']/div[2]//span/text()").extract()
        for i,j in zip(content,price):
            print(i,j)


