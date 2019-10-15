# -*- coding: utf-8 -*-
import scrapy
from novelspider.items import NovelspiderItem
import re


class NovelspiderSpider(scrapy.Spider):
    name = 'novelspider'
    allowed_domains = ['www.qu.la']
    start_urls = ['https://www.qu.la/book/16431/6658470.html']

    def parse(self, response):
        item = NovelspiderItem()
        item['title'] = response.xpath("//div[@class='bookname']/h1/text()").extract()
        item['content'] = response.xpath("//div[@id='content']/text()").extract()
        yield item

        link = response.xpath("//a[@class='next' and @id='A3' and @target='_top']/@href").extract()[0]
        if not re.match(r'./', link):
            yield scrapy.Request("https://www.qu.la/book/382/" + link, callback=self.parse)
        else:
            print('Save finished!')

