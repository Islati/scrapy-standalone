# -*- coding: utf-8 -*-
import json

from scrapy import Request
from scrapy.crawler import CrawlerProcess
from scrapy.loader import ItemLoader
from scrapy import log, signals, Spider, Item, Field
from scrapy.settings import Settings
from twisted.internet import reactor

_SPIDER_NAME = "{{cookiecutter.script_name}}"


# define an item class
class {{cookiecutter.script_name | title}}Item(Item):
    field = Field()


class {{cookiecutter.script_name | title}}Spider(Spider):
    name = _SPIDER_NAME
    allowed_domains = ["{{cookiecutter.allowed_domain}}"]

    def start_requests(self):
        yield Request("{{cookiecutter.allowed_domain}}", callback=self.parse)

    def parse(self, response):
        pass


process = CrawlerProcess({
    'COOKIES_ENABLED': False,
    'SPIDER_MIDDLEWARES': {
        'scrapy.contrib.spidermiddleware.referer.RefererMiddleware': True
    }
    {% if cookiecutter.use_crawlera == true %}
    ,'DOWNLOADER_MIDDLEWARES': {
        'scrapy_crawlera.CrawleraMiddleware': 610
    },
    'CRAWLERA_ENABLED': True,
    'CRAWLERA_APIKEY': '{{cookiecutter.crawlera_api_key}}'
    {% endif %}
})

process.crawl({{cookiecutter.script_name | title}}Spider)
process.start()