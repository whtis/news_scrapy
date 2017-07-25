import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from rss_news.items import ArticleItem


class RssSpider(CrawlSpider):
    name = "rss"

    def __init__(self, rule):
        self.rule = rule
        self.name = rule.site_name
        self.allowed_domains = rule.allow_domains.split(",")
        self.start_urls = rule.start_urls.split(",")
        rule_list = []
        # 添加`下一页`的规则
        if rule.next_page:
            rule_list.append(Rule(LinkExtractor(restrict_xpaths=rule.next_page)))
        # 添加抽取文章链接的规则
        rule_list.append(Rule(LinkExtractor(
            allow=[rule.allow_url],
            restrict_xpaths=[rule.extract_from]),
            callback='parse_item', follow=True))
        self.rules = tuple(rule_list)
        super(RssSpider, self).__init__()

    def parse_item(self, response):
        self.log('Hi, this is a rss page! %s' % response.url)

        selector = scrapy.Selector(response)
        contents = selector.xpath('//channel/item')
        for infos in contents:
            article = ArticleItem()

            article["url"] = response.url

            title = infos.xpath('title/text()').extract()
            article["title"] = title[0] if title else ""

            content = infos.xpath(self.rule.content_xpath).extract()
            article["content"] = content[0] if content else ""

            publish_time = infos.xpath(self.rule.publish_time_xpath).extract()
            article["publish_time"] = publish_time[0] if publish_time else ""

            category = infos.xpath('category/text()').extract()[0]
            article["category"] = category[0] if category else ""

            link = infos.xpath('link/text()').extract()[0]
            author = infos.xpath('author/text()').extract()
            article["author"] = author[0] if category else ""

            yield article
