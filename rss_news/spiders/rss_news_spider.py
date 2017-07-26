# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy import Request

from items import ArticleItem
from utils.content import filter_html_tags


class RssSpider(scrapy.Spider):
    name = 'rss'
    start_urls = ['http://www.wyzxwk.com/e/web/?type=rss2&classid=0']

    def parse(self, response):
        if re.match(r'http://www\.wyzxwk\.com/e/web/\?type=rss2&classid=0', response.url):
            yield Request(response.url, callback=self.parse_rss)
        elif re.match(r'http://www\.wyzxwk\.com/Article(.*)\.html', response.url):
            yield Request(response.url, callback=self.parse_details)

    def parse_rss(self, response):
        selector = scrapy.Selector(response)
        contents = selector.xpath('//channel/item')
        for content in contents:
            title = content.xpath('title/text()').extract()[0]
            link = content.xpath('link/text()').extract()[0]
            category = content.xpath('category/text()').extract()[0]
            author = content.xpath('author/text()').extract()[0]
            pubDate = content.xpath('pubDate/text()').extract()[0]

            article = ArticleItem()
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
        print(article)
