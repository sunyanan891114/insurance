# -*- coding: utf-8 -*-
import scrapy
from ..items import InsuranceItem


class QuestionSpider(scrapy.Spider):
    name = 'question'
    allowed_domains = ['www.circ.gov.cn']
    start_urls = ['http://www.circ.gov.cn/web/site47/tab4313/']
    rules = (
        scrapy.spiders.Rule(scrapy.linkextractors.LinkExtractor()),
        scrapy.spiders.Rule(scrapy.linkextractors.LinkExtractor(allow=('item\.php',)), callback='parse_item'),
    )

    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        title = response.css("#ess_ctr12344_ModuleContent > tbody > tr > td > table.normal > tbody > tr:nth-child(1) > td").extract_first()
        answer = response.css("#zoom > p").extract_first()
        print('----------------------')
        print(title)
        print('-------------------------')
        print(answer)
        yield InsuranceItem(title=title, answer=answer)
