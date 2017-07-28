# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from rss_news.config.mysql import DBSession
from rss_news.model.article_model import ArticleModel


# 存储到数据库
class DataBasePipeline(object):
    def open_spider(self, spider):
        self.session = DBSession()

    def process_item(self, item, spider):
        ArticleModel.__table__.name = item['table_name']
        a = ArticleModel(title=item["title"].encode("utf-8"),
                         category=item["category"].encode("utf-8"),
                         url=item["url"],
                         author=item["author"].encode("utf-8"),
                         content=item["content"].encode("utf-8"),
                         publish_time=item["publish_time"])
        self.session.add(a)
        self.session.commit()

    def close_spider(self, spider):
        self.session.close()
