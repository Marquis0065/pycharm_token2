# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DangdangPipeline:
    #爬虫文件开始前执行的方法
    def open_spider(self,spider):
        self.fp=open('book6.json','w',encoding='utf8')
    def process_item(self, item, spider):
        #下面的方法不推荐，需多次打开文件
        # with open('book.json','a',encoding='utf8')as fp:
        #     #写入的必须是字符串，不能是对象
        #     fp.write(str(item))
        self.fp.write(str(item))
        return item
    #在爬虫文件执行完毕后，执行的方法
    def close_spider(self,spider):
        self.fp.close()

import urllib.request
class   imgDownload:
    def process_item(self, item, spider):
        url = item.get('src')
        name = item.get('name')
        filename = './bookstore/'+name+'.jpg'
        urllib.request.urlretrieve(url = url ,filename=filename)
        return item