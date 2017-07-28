# -*- coding: utf-8 -*-
import datetime
import re
import scrapy
import time
from scrapy import Request
import logging

from items import ArticleItem
from utils.content import filter_html_tags


class RssSpider(scrapy.Spider):
    name = 'rss'
    start_urls = [
        # 'http://www.wyzxwk.com/e/web/?type=rss2&classid=0',
        'http://www.szhgh.com/e/web/?type=rss2'
    ]

    def parse(self, response):
        if response.url.find('rss') != -1:
            yield Request(response.url, callback=self.parse_rss)
        elif response.url.find('Article') != -1:
            yield Request(response.url, callback=self.parse_details)
        else:
            self.logger.info('start urls is not useful, please check it!')

    def parse_rss(self, response):
        selector = scrapy.Selector(response)
        contents = selector.xpath('//channel/item')
        for content in contents:
            title = content.xpath('title/text()').extract()[0]
            link = content.xpath('link/text()').extract()[0]
            category = content.xpath('category/text()').extract()[0]
            author = content.xpath('author/text()').extract()[0]
            pubDate = content.xpath('pubDate/text()').extract()[0]
            # 转换为时间戳
            pub_float = time.mktime(time.strptime(pubDate, '%a, %d %b %Y %X %z'))
            timestamp = time.strftime('%Y-%m-%d %X', time.localtime(pub_float))
            # timestamp = datetime.datetime.fromtimestamp(pub_float).strftime('%Y-%m-%d %H:%M:%S')
            '''
            时间戳是一个str类型，因此格式化原时间后，需要使用上面两个语句之一还原成str
            '''
            table_name = 'none'
            if response.url.find('wyzx') != -1:
                table_name = 'wyzx'
            elif response.url.find('szhgh') != -1:
                table_name = 'szhgh'
            else:
                return
            article = ArticleItem()
            article['table_name'] = 'article_' + table_name.lower()
            article['title'] = title
            article['category'] = category
            article['url'] = link
            article['author'] = author
            article['publish_time'] = timestamp
            if link is not None:
                yield scrapy.http.Request(url=link, meta={'item': article}, callback=self.parse_details)

    def parse_details(self, response):
        article = response.meta['item']
        selector = scrapy.Selector(response)
        content = selector.xpath('//div[@class="m-article s-shadow"]/article/p').extract().__str__()
        # 正则过滤html字符串
        content = content.replace("', '", "").replace("\\u3000", "  ").replace("'", "").replace("\\xa0", "") \
            .replace("▍", "")
        content = filter_html_tags(content)
        article['content'] = content
        return article
