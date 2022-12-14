# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class ScrapyReadbookPipeline:

    def process_item(self, item, spider):
        with open('book.json','a',encoding='utf8')as fp:
            fp.write(str(item))
        return item

from scrapy.utils.project import get_project_settings

class MysqlPipeline:
    def open_spider(self,spider):
        settings = get_project_settings()
        # DB_HOST = '192.168.1.4'
        # DB_PROT = 3306
        # DB_USER = 'root'
        # DB_PASSWORD = '1qaz@WSX'
        # DB_NAME = 'spider1'
        # DB_CHARSET = 'utf8'
        self.host=settings['DB_HOST']
        self.port=settings['DB_PROT']
        self.user=settings['DB_USER']
        self.password=settings['DB_PASSWORD']
        self.name=settings['DB_NAME']
        self.charset=settings['DB_CHARSET']
        #连接
        self.connect()
    def connect(self):
        self.conn =pymysql.connect(
            host= self.host,
            port = self.port,
            user=self.user,
            password= self.password,
            db=self.name,
            charset=self.charset

        )
        self.cursor = self.conn.cursor()


    def process_item(self,item,spider):
        sql = 'insert into book(name,src)values("{}","{}")'.format(item['name'],item['src'])
        #执行sql语句
        self.cursor.execute(sql)
        self.conn.commit()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()