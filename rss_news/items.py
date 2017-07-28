# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticleItem(scrapy.Item):
    aid = scrapy.Field()
    title = scrapy.Field()
    category = scrapy.Field()
    url = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
    publish_time = scrapy.Field()
    source_site = scrapy.Field()
    table_name = scrapy.Field()
    extra1 = scrapy.Field()
    extra2 = scrapy.Field()
    extra3 = scrapy.Field()
