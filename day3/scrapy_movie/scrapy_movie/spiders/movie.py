import scrapy
from scrapy_movie.items import ScrapyMovieItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['www.ygdy8.net']
    start_urls = ['https://www.ygdy8.net/html/gndy/china/index.html']


    def parse(self, response):
        for i in response.xpath('//a[@class="ulink"][2]'):
            name = i.xpath('./text()').extract_first()
            href = i.xpath('./@href').extract_first()
            print(href)
            #第二页地址
            url = 'https://www.ygdy8.net'+href
            print(url)
            yield scrapy.Request(url = url,callback=self.parse_second,meta={'name':name})

    def parse_second(self, response):
        src = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        name = response.meta['name']
        movie = ScrapyMovieItem(src=src, name=name)
        print(name,src)
        yield movie


