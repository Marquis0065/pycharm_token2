# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Lianjia1215Pipeline:
    def process_item(self, item, spider):
        with open('longhua.txt','a',encoding='utf8')as fp:
            fp.write(str(item))
        return item
