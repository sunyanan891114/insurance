# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import InsuranceItem


class QuestionSpider(scrapy.Spider):
    name = 'question'
    allowed_domains = ['www.circ.gov.cn']
    start_urls = ['http://www.circ.gov.cn/web/site47/tab4313/']
    base_url = 'http://www.circ.gov.cn'

    def parse(self, response):
        links = response.css('a::attr(href)').extract()
        for i in links:
            if i.find(self.base_url) == -1:
                i = self.base_url + i

            yield scrapy.Request(response.urljoin(i), callback=self.parse_item)

    def parse_item(self, response):
        title = response.css("#ess_ctr12344_ModuleContent table.normal tbody > tr:nth-child(1) > td")\
            .css('::text').extract_first()
        answer = reduce(remove_empty, response.css("#zoom p").css('::text').extract(), '')

        if answer and title is not None:
            yield InsuranceItem(answer=answer, url=response.url, title=title)
        else:
            links = response.css('a::attr(href)').extract()
            for i in links:
                if i.find(self.base_url) == -1:
                    i = self.base_url + i
                if i.find('site47') > 0:
                    yield scrapy.Request(response.urljoin(i), callback=self.parse_item)


def remove_empty(result, current):
    text = current.replace(" ", "")
    if text is not "":
        return result + current
    else:
        return result
