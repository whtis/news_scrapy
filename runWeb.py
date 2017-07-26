# -*- coding: utf-8 -*-
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from rss_news.config.mysql import DBSession
from rss_news.model.rule_model import Rule
from rss_news.spiders.web_news_spider import WebSpider

# run webSpider
settings = Settings()
settings.set("ITEM_PIPELINES", {
    # 'pipelines.DuplicatesPipeline': 200,
    # 'pipelines.CountDropPipline': 100,
    'pipelines.DataBasePipeline': 300,
})
# crawl settings
settings.set("USER_AGENT",
             "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari"
             "/537.36")

process = CrawlerProcess(settings)

db = DBSession()
rules = db.query(Rule).filter(Rule.enable == 1)
for rule in rules:
    process.crawl(WebSpider, rule)
process.start()
