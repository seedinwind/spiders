# -*- coding: gbk -*-

import scrapy


class dzjSpider(scrapy.Spider):
    name = 'dzj'
    allowed_domains = ['www.qldzj.com']
    start_urls = [
        'http://www.qldzj.com/html/ml01.htm'
        # 'https://so.gushiwen.org/authors/authorvsw_1abe13750637A1.aspx',
    ]

    def start_request(self):
        for url in start_urls:
            yield scrapy.Request(url, callback=self.parse, headers=self.headers)

    def parse(self, response):
